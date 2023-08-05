from __future__ import annotations

from typing import Literal

from prettyqt import core, positioning
from prettyqt.qt import QtLocation
from prettyqt.utils import InvalidParamError, bidict


FEATURE_TYPES = bidict(
    none=QtLocation.QGeoRouteRequest.FeatureType.NoFeature,
    toll=QtLocation.QGeoRouteRequest.FeatureType.TollFeature,
    highway=QtLocation.QGeoRouteRequest.FeatureType.HighwayFeature,
    public_transit=QtLocation.QGeoRouteRequest.FeatureType.PublicTransitFeature,
    ferry=QtLocation.QGeoRouteRequest.FeatureType.FerryFeature,
    tunnel=QtLocation.QGeoRouteRequest.FeatureType.TunnelFeature,
    dirt_road=QtLocation.QGeoRouteRequest.FeatureType.DirtRoadFeature,
    parks=QtLocation.QGeoRouteRequest.FeatureType.ParksFeature,
    motor_pool_lane=QtLocation.QGeoRouteRequest.FeatureType.MotorPoolLaneFeature,
    traffic=QtLocation.QGeoRouteRequest.FeatureType.TrafficFeature,
)

FeatureTypeStr = Literal[
    "none",
    "toll",
    "highway",
    "public_transit",
    "ferry",
    "tunnel",
    "dirt_road",
    "parks",
    "motor_pool_lane",
    "traffic",
]

FEATURE_WEIGHTS = bidict(
    neutral=QtLocation.QGeoRouteRequest.FeatureWeight.NeutralFeatureWeight,
    prefer=QtLocation.QGeoRouteRequest.FeatureWeight.PreferFeatureWeight,
    require=QtLocation.QGeoRouteRequest.FeatureWeight.RequireFeatureWeight,
    avoid=QtLocation.QGeoRouteRequest.FeatureWeight.AvoidFeatureWeight,
    disallow=QtLocation.QGeoRouteRequest.FeatureWeight.DisallowFeatureWeight,
)

FeatureWeightStr = Literal["neutral", "prefer", "require", "avoid", "disallow"]

MANEUVER_DETAIL = bidict(
    none=QtLocation.QGeoRouteRequest.ManeuverDetail.NoManeuvers,
    basic=QtLocation.QGeoRouteRequest.ManeuverDetail.BasicManeuvers,
)

ManeuverDetailStr = Literal["none", "basic"]

ROUTE_OPTIMIZATION = bidict(
    shortest=QtLocation.QGeoRouteRequest.RouteOptimization.ShortestRoute,
    fastest=QtLocation.QGeoRouteRequest.RouteOptimization.FastestRoute,
    most_economic=QtLocation.QGeoRouteRequest.RouteOptimization.MostEconomicRoute,
    most_scenic=QtLocation.QGeoRouteRequest.RouteOptimization.MostScenicRoute,
)

RouteOptimizationStr = Literal["shortest", "fastest", "most_economic", "most_scenic"]

SEGMENT_DETAIL = bidict(
    none=QtLocation.QGeoRouteRequest.SegmentDetail.NoSegmentData,
    basic=QtLocation.QGeoRouteRequest.SegmentDetail.BasicSegmentData,
)

SegmentDetailStr = Literal["none", "basic"]

TRAVEL_MODE = bidict(
    car=QtLocation.QGeoRouteRequest.TravelMode.CarTravel,
    pedestrian=QtLocation.QGeoRouteRequest.TravelMode.PedestrianTravel,
    bicycle=QtLocation.QGeoRouteRequest.TravelMode.BicycleTravel,
    public_transit=QtLocation.QGeoRouteRequest.TravelMode.PublicTransitTravel,
    truck=QtLocation.QGeoRouteRequest.TravelMode.TruckTravel,
)

TravelModeStr = Literal["car", "pedestrian", "bicycle", "public_transit", "truck"]


class GeoRouteRequest(QtLocation.QGeoRouteRequest):
    def get_waypoints(self) -> list[positioning.GeoCoordinate]:
        return [positioning.GeoCoordinate(wp) for wp in self.waypoints()]

    def get_exclude_areas(self) -> list[positioning.GeoRectangle]:
        return [positioning.GeoRectangle(wp) for wp in self.excludeAreas()]

    def get_departure_time(self) -> core.DateTime:
        return core.DateTime(self.departureTime())

    def set_feature_weight(self, feature: FeatureTypeStr, weight: FeatureWeightStr):
        """Set the feature weight.

        Args:
            feature: Feature type
            weight: Feature weight

        Raises:
            InvalidParamError: feature weight / type does not exist
        """
        if weight not in FEATURE_WEIGHTS:
            raise InvalidParamError(weight, FEATURE_WEIGHTS)
        if feature not in FEATURE_TYPES:
            raise InvalidParamError(feature, FEATURE_TYPES)
        self.setFeatureWeight(FEATURE_TYPES[feature], FEATURE_WEIGHTS[weight])

    def get_feature_weight(self, feature: FeatureTypeStr) -> FeatureWeightStr:
        """Return current feature weight.

        Returns:
            Feature weight
        """
        if feature not in FEATURE_TYPES:
            raise InvalidParamError(feature, FEATURE_TYPES)
        return FEATURE_WEIGHTS.inverse[self.featureWeight(FEATURE_TYPES[feature])]

    def set_route_optimization(self, optimization: RouteOptimizationStr):
        """Set the route optimization.

        Args:
            optimization: Route optimization

        Raises:
            InvalidParamError: route optimization does not exist
        """
        if optimization not in ROUTE_OPTIMIZATION:
            raise InvalidParamError(optimization, ROUTE_OPTIMIZATION)
        self.setRouteOptimization(ROUTE_OPTIMIZATION[optimization])

    def get_route_optimization(self) -> RouteOptimizationStr:
        """Return current route optimization.

        Returns:
            Route optimization
        """
        return ROUTE_OPTIMIZATION.inverse[self.routeOptimization()]

    def get_travel_modes(self) -> list[TravelModeStr]:
        return TRAVEL_MODE.get_list(self.travelModes())

    def set_travel_modes(self, *mode: TravelModeStr):
        for item in mode:
            if item not in TRAVEL_MODE:
                raise InvalidParamError(item, TRAVEL_MODE)
        flags = TRAVEL_MODE.merge_flags(mode)
        self.setTravelModes(flags)

    def get_feature_types(self) -> list[FeatureTypeStr]:
        return [k for k, v in FEATURE_TYPES.items() for t in self.featureTypes() if v & t]


if __name__ == "__main__":
    request = GeoRouteRequest()
