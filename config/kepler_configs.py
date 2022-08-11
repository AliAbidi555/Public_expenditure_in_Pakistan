karachi_grid_property_value = {
  "version": "v1",
  "config": {
    "visState": {
      "filters": [],
      "layers": [
        {
          "id": "jxz01ap",
          "type": "geojson",
          "config": {
            "dataId": "grid_property",
            "label": "grid_property",
            "color": [
              18,
              147,
              154
            ],
            "columns": {
              "geojson": "geometry"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 0.24,
              "strokeOpacity": 0.8,
              "thickness": 0.5,
              "strokeColor": [
                221,
                178,
                124
              ],
              "colorRange": {
                "name": "ColorBrewer YlGn-3",
                "type": "sequential",
                "category": "ColorBrewer",
                "colors": [
                  "#f7fcb9",
                  "#addd8e",
                  "#31a354"
                ]
              },
              "strokeColorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "radius": 10,
              "sizeRange": [
                0,
                10
              ],
              "radiusRange": [
                0,
                50
              ],
              "heightRange": [
                0,
                500
              ],
              "elevationScale": 5,
              "stroked": False,
              "filled": True,
              "enable3d": False,
              "wireframe": False
            },
            "hidden": False,
            "textLabel": [
              {
                "field": None,
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 18,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center"
              }
            ]
          },
          "visualChannels": {
            "colorField": {
              "name": "res_value_sqyard",
              "type": "integer"
            },
            "colorScale": "quantile",
            "sizeField": None,
            "sizeScale": "linear",
            "strokeColorField": None,
            "strokeColorScale": "quantile",
            "heightField": None,
            "heightScale": "linear",
            "radiusField": None,
            "radiusScale": "linear"
          }
        }
      ],
      "interactionConfig": {
        "tooltip": {
          "fieldsToShow": {
            "grid_property": [
              {
                "name": "vor_id",
                "format": None
              },
              {
                "name": "area_sq",
                "format": None
              },
              {
                "name": "area_sqrt",
                "format": None
              },
              {
                "name": "res_value_sqyard",
                "format": None
              },
              {
                "name": "com_value_sqyard",
                "format": None
              }
            ]
          },
          "compareMode": False,
          "compareType": "absolute",
          "enabled": True
        },
        "brush": {
          "size": 0.5,
          "enabled": False
        },
        "geocoder": {
          "enabled": False
        },
        "coordinate": {
          "enabled": False
        }
      },
      "layerBlending": "normal",
      "splitMaps": [],
      "animationConfig": {
        "currentTime": None,
        "speed": 1
      }
    },
    "mapState": {
      "bearing": 0,
      "dragRotate": False,
      "latitude": 25.002878548501467,
      "longitude": 67.10461958958498,
      "pitch": 0,
      "zoom": 9.143415104929465,
      "isSplit": False
    },
    "mapStyle": {
      "styleType": "light",
      "topLayerGroups": {},
      "visibleLayerGroups": {
        "label": True,
        "road": True,
        "border": False,
        "building": True,
        "water": True,
        "land": True,
        "3d building": False
      },
      "threeDBuildingColor": [
        218.82023004728686,
        223.47597962276103,
        223.47597962276103
      ],
      "mapStyles": {}
    }
  }
}


islamabad_grid_population_fb = {
  "version": "v1",
  "config": {
    "visState": {
      "filters": [],
      "layers": [
        {
          "id": "x1yr7q4",
          "type": "geojson",
          "config": {
            "dataId": "fb_pop_data",
            "label": "fb_pop_data",
            "color": [
              18,
              147,
              154
            ],
            "columns": {
              "geojson": "geometry"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 0.49,
              "strokeOpacity": 0.8,
              "thickness": 0.5,
              "strokeColor": [
                221,
                178,
                124
              ],
              "colorRange": {
                "name": "ColorBrewer YlGn-6",
                "type": "sequential",
                "category": "ColorBrewer",
                "colors": [
                  "#ffffcc",
                  "#d9f0a3",
                  "#addd8e",
                  "#78c679",
                  "#31a354",
                  "#006837"
                ]
              },
              "strokeColorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "radius": 10,
              "sizeRange": [
                0,
                10
              ],
              "radiusRange": [
                0,
                50
              ],
              "heightRange": [
                0,
                500
              ],
              "elevationScale": 5,
              "stroked": False,
              "filled": True,
              "enable3d": False,
              "wireframe": False
            },
            "hidden": False,
            "textLabel": [
              {
                "field": None,
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 18,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center"
              }
            ]
          },
          "visualChannels": {
            "colorField": {
              "name": "sum_pop_general",
              "type": "real"
            },
            "colorScale": "quantile",
            "sizeField": None,
            "sizeScale": "linear",
            "strokeColorField": None,
            "strokeColorScale": "quantile",
            "heightField": None,
            "heightScale": "linear",
            "radiusField": None,
            "radiusScale": "linear"
          }
        }
      ],
      "interactionConfig": {
        "tooltip": {
          "fieldsToShow": {
            "fb_pop_data": [
              {
                "name": "vor_id",
                "format": None
              },
              {
                "name": "sum_pop_youth",
                "format": None
              },
              {
                "name": "mean_pop_youth",
                "format": None
              },
              {
                "name": "max_pop_youth",
                "format": None
              },
              {
                "name": "min_pop_youth",
                "format": None
              }
            ]
          },
          "compareMode": False,
          "compareType": "absolute",
          "enabled": True
        },
        "brush": {
          "size": 0.5,
          "enabled": False
        },
        "geocoder": {
          "enabled": False
        },
        "coordinate": {
          "enabled": False
        }
      },
      "layerBlending": "normal",
      "splitMaps": [],
      "animationConfig": {
        "currentTime": None,
        "speed": 1
      }
    },
    "mapState": {
      "bearing": 0,
      "dragRotate": False,
      "latitude": 33.63867036458851,
      "longitude": 73.14774496451345,
      "pitch": 0,
      "zoom": 10.334939641138217,
      "isSplit": False
    },
    "mapStyle": {
      "styleType": "light",
      "topLayerGroups": {},
      "visibleLayerGroups": {
        "label": True,
        "road": True,
        "border": False,
        "building": True,
        "water": True,
        "land": True,
        "3d building": False
      },
      "threeDBuildingColor": [
        218.82023004728686,
        223.47597962276103,
        223.47597962276103
      ],
      "mapStyles": {}
    }
  }
}

islamabad_grid_property_value_config = {
  "version": "v1",
  "config": {
    "visState": {
      "filters": [],
      "layers": [
        {
          "id": "5jzzt4",
          "type": "geojson",
          "config": {
            "dataId": "grid_values",
            "label": "grid_values",
            "color": [
              18,
              147,
              154
            ],
            "columns": {
              "geojson": "geometry"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 0.36,
              "strokeOpacity": 0.8,
              "thickness": 0.5,
              "strokeColor": [
                221,
                178,
                124
              ],
              "colorRange": {
                "name": "ColorBrewer YlGn-3",
                "type": "sequential",
                "category": "ColorBrewer",
                "colors": [
                  "#f7fcb9",
                  "#addd8e",
                  "#31a354"
                ]
              },
              "strokeColorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "radius": 10,
              "sizeRange": [
                0,
                10
              ],
              "radiusRange": [
                0,
                50
              ],
              "heightRange": [
                0,
                500
              ],
              "elevationScale": 5,
              "stroked": False,
              "filled": True,
              "enable3d": False,
              "wireframe": False
            },
            "hidden": False,
            "textLabel": [
              {
                "field": None,
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 18,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center"
              }
            ]
          },
          "visualChannels": {
            "colorField": {
              "name": "res_value_sqyard",
              "type": "integer"
            },
            "colorScale": "quantile",
            "sizeField": None,
            "sizeScale": "linear",
            "strokeColorField": None,
            "strokeColorScale": "quantile",
            "heightField": None,
            "heightScale": "linear",
            "radiusField": None,
            "radiusScale": "linear"
          }
        }
      ],
      "interactionConfig": {
        "tooltip": {
          "fieldsToShow": {
            "grid_values": [
              {
                "name": "vor_id",
                "format": None
              },
              {
                "name": "com_value_sqyard",
                "format": None
              },
              {
                "name": "area_sq",
                "format": None
              },
              {
                "name": "area_sqrt",
                "format": None
              },
              {
                "name": "res_value_sqyard",
                "format": None
              }
            ]
          },
          "compareMode": False,
          "compareType": "absolute",
          "enabled": True
        },
        "brush": {
          "size": 0.5,
          "enabled": False
        },
        "geocoder": {
          "enabled": False
        },
        "coordinate": {
          "enabled": False
        }
      },
      "layerBlending": "normal",
      "splitMaps": [],
      "animationConfig": {
        "currentTime": None,
        "speed": 1
      }
    },
    "mapState": {
      "bearing": 0,
      "dragRotate": False,
      "latitude": 33.66984436599593,
      "longitude": 73.0939549518392,
      "pitch": 0,
      "zoom": 10.442426301685865,
      "isSplit": False
    },
    "mapStyle": {
      "styleType": "light",
      "topLayerGroups": {},
      "visibleLayerGroups": {
        "label": True,
        "road": True,
        "border": False,
        "building": True,
        "water": True,
        "land": True,
        "3d building": False
      },
      "threeDBuildingColor": [
        218.82023004728686,
        223.47597962276103,
        223.47597962276103
      ],
      "mapStyles": {}
    }
  }
}

lahore_grid_property_value_config = {
  "version": "v1",
  "config": {
    "visState": {
      "filters": [],
      "layers": [
        {
          "id": "3krkzx",
          "type": "geojson",
          "config": {
            "dataId": "grid_values",
            "label": "grid_values",
            "color": [
              18,
              147,
              154
            ],
            "columns": {
              "geojson": "geometry"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 0.8,
              "strokeOpacity": 0.8,
              "thickness": 0.5,
              "strokeColor": [
                221,
                178,
                124
              ],
              "colorRange": {
                "name": "ColorBrewer YlGn-3",
                "type": "sequential",
                "category": "ColorBrewer",
                "colors": [
                  "#f7fcb9",
                  "#addd8e",
                  "#31a354"
                ]
              },
              "strokeColorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "radius": 10,
              "sizeRange": [
                0,
                10
              ],
              "radiusRange": [
                0,
                50
              ],
              "heightRange": [
                0,
                500
              ],
              "elevationScale": 5,
              "stroked": False,
              "filled": True,
              "enable3d": False,
              "wireframe": False
            },
            "hidden": False,
            "textLabel": [
              {
                "field": None,
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 18,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center"
              }
            ]
          },
          "visualChannels": {
            "colorField": {
              "name": "res_value_marla",
              "type": "integer"
            },
            "colorScale": "quantile",
            "sizeField": None,
            "sizeScale": "linear",
            "strokeColorField": None,
            "strokeColorScale": "quantile",
            "heightField": None,
            "heightScale": "linear",
            "radiusField": None,
            "radiusScale": "linear"
          }
        }
      ],
      "interactionConfig": {
        "tooltip": {
          "fieldsToShow": {
            "grid_values": [
              {
                "name": "vor_id",
                "format": None
              },
              {
                "name": "area_sq",
                "format": None
              },
              {
                "name": "area_sqrt",
                "format": None
              },
              {
                "name": "res_value_marla",
                "format": None
              },
              {
                "name": "com_value_marla",
                "format": None
              }
            ]
          },
          "compareMode": False,
          "compareType": "absolute",
          "enabled": True
        },
        "brush": {
          "size": 0.5,
          "enabled": False
        },
        "geocoder": {
          "enabled": False
        },
        "coordinate": {
          "enabled": False
        }
      },
      "layerBlending": "normal",
      "splitMaps": [],
      "animationConfig": {
        "currentTime": None,
        "speed": 1
      }
    },
    "mapState": {
      "bearing": 0,
      "dragRotate": False,
      "latitude": 31.50937016705192,
      "longitude": 74.3182621689959,
      "pitch": 0,
      "zoom": 9.802629055864404,
      "isSplit": False
    },
    "mapStyle": {
      "styleType": "light",
      "topLayerGroups": {},
      "visibleLayerGroups": {
        "label": True,
        "road": True,
        "border": False,
        "building": True,
        "water": True,
        "land": True,
        "3d building": False
      },
      "threeDBuildingColor": [
        218.82023004728686,
        223.47597962276103,
        223.47597962276103
      ],
      "mapStyles": {}
    }
  }
}




lahore_property_data = {
  "version": "v1",
  "config": {
    "visState": {
      "filters": [],
      "layers": [
        {
          "id": "euirdw",
          "type": "geojson",
          "config": {
            "dataId": "boundaries",
            "label": "boundaries_res",
            "color": [
              18,
              147,
              154
            ],
            "columns": {
              "geojson": "geometry"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 0.8,
              "strokeOpacity": 0.8,
              "thickness": 0.5,
              "strokeColor": [
                221,
                178,
                124
              ],
              "colorRange": {
                "name": "ColorBrewer YlGn-3",
                "type": "sequential",
                "category": "ColorBrewer",
                "colors": [
                  "#f7fcb9",
                  "#addd8e",
                  "#31a354"
                ]
              },
              "strokeColorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "radius": 10,
              "sizeRange": [
                0,
                10
              ],
              "radiusRange": [
                0,
                50
              ],
              "heightRange": [
                0,
                500
              ],
              "elevationScale": 5,
              "stroked": False,
              "filled": True,
              "enable3d": False,
              "wireframe": False
            },
            "hidden": False,
            "textLabel": [
              {
                "field": None,
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 18,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center"
              }
            ]
          },
          "visualChannels": {
            "colorField": {
              "name": "res_value_marla",
              "type": "integer"
            },
            "colorScale": "quantile",
            "sizeField": None,
            "sizeScale": "linear",
            "strokeColorField": None,
            "strokeColorScale": "quantile",
            "heightField": None,
            "heightScale": "linear",
            "radiusField": None,
            "radiusScale": "linear"
          }
        },
        {
          "id": "fy1oicv",
          "type": "geojson",
          "config": {
            "dataId": "boundaries",
            "label": "boundaries_com",
            "color": [
              119,
              110,
              87
            ],
            "columns": {
              "geojson": "geometry"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 0.8,
              "strokeOpacity": 0.8,
              "thickness": 0.5,
              "strokeColor": None,
              "colorRange": {
                "name": "ColorBrewer YlGn-3",
                "type": "sequential",
                "category": "ColorBrewer",
                "colors": [
                  "#f7fcb9",
                  "#addd8e",
                  "#31a354"
                ]
              },
              "strokeColorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "radius": 10,
              "sizeRange": [
                0,
                10
              ],
              "radiusRange": [
                0,
                50
              ],
              "heightRange": [
                0,
                500
              ],
              "elevationScale": 5,
              "stroked": False,
              "filled": True,
              "enable3d": False,
              "wireframe": False
            },
            "hidden": False,
            "textLabel": [
              {
                "field": None,
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 18,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center"
              }
            ]
          },
          "visualChannels": {
            "colorField": {
              "name": "com_value_marla",
              "type": "integer"
            },
            "colorScale": "quantile",
            "sizeField": None,
            "sizeScale": "linear",
            "strokeColorField": None,
            "strokeColorScale": "quantile",
            "heightField": None,
            "heightScale": "linear",
            "radiusField": None,
            "radiusScale": "linear"
          }
        }
      ],
      "interactionConfig": {
        "tooltip": {
          "fieldsToShow": {
            "boundaries": [
              {
                "name": "aid",
                "format": None
              },
              {
                "name": "index_right",
                "format": None
              },
              {
                "name": "area",
                "format": None
              },
              {
                "name": "res_value_marla",
                "format": None
              },
              {
                "name": "com_value_marla",
                "format": None
              }
            ],
            "properties": [
              {
                "name": "area",
                "format": None
              },
              {
                "name": "res_value_marla",
                "format": None
              },
              {
                "name": "com_value_marla",
                "format": None
              },
              {
                "name": "address",
                "format": None
              },
              {
                "name": "drop",
                "format": None
              }
            ]
          },
          "compareMode": False,
          "compareType": "absolute",
          "enabled": True
        },
        "brush": {
          "size": 0.5,
          "enabled": False
        },
        "geocoder": {
          "enabled": False
        },
        "coordinate": {
          "enabled": False
        }
      },
      "layerBlending": "normal",
      "splitMaps": [
        {
          "layers": {
            "euirdw": True,
            "fy1oicv": False
          }
        },
        {
          "layers": {
            "euirdw": False,
            "fy1oicv": True
          }
        }
      ],
      "animationConfig": {
        "currentTime": None,
        "speed": 1
      }
    },
    "mapState": {
      "bearing": 0,
      "dragRotate": False,
      "latitude": 31.57433436047517,
      "longitude": 74.35551965828965,
      "pitch": 0,
      "zoom": 8.972397911525567,
      "isSplit": True
    },
    "mapStyle": {
      "styleType": "light",
      "topLayerGroups": {},
      "visibleLayerGroups": {
        "label": True,
        "road": True,
        "border": False,
        "building": True,
        "water": True,
        "land": True,
        "3d building": False
      },
      "threeDBuildingColor": [
        218.82023004728686,
        223.47597962276103,
        223.47597962276103
      ],
      "mapStyles": {}
    }
  }
}




lahore_fb_data_compare = {
  "version": "v1",
  "config": {
    "visState": {
      "filters": [],
      "layers": [
        {
          "id": "ie5oopl",
          "type": "geojson",
          "config": {
            "dataId": "fb_stats",
            "label": "fb_stats_general",
            "color": [
              18,
              147,
              154
            ],
            "columns": {
              "geojson": "geometry"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 0.8,
              "strokeOpacity": 0.8,
              "thickness": 0.3,
              "strokeColor": [
                192,
                192,
                192
              ],
              "colorRange": {
                "name": "ColorBrewer RdYlGn-11",
                "type": "diverging",
                "category": "ColorBrewer",
                "colors": [
                  "#006837",
                  "#1a9850",
                  "#66bd63",
                  "#a6d96a",
                  "#d9ef8b",
                  "#ffffbf",
                  "#fee08b",
                  "#fdae61",
                  "#f46d43",
                  "#d73027",
                  "#a50026"
                ],
                "reversed": True
              },
              "strokeColorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "radius": 10,
              "sizeRange": [
                0,
                10
              ],
              "radiusRange": [
                0,
                50
              ],
              "heightRange": [
                0,
                500
              ],
              "elevationScale": 5,
              "stroked": True,
              "filled": True,
              "enable3d": False,
              "wireframe": False
            },
            "hidden": False,
            "textLabel": [
              {
                "field": None,
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 18,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center"
              }
            ]
          },
          "visualChannels": {
            "colorField": {
              "name": "sum_pop_general",
              "type": "real"
            },
            "colorScale": "quantile",
            "sizeField": None,
            "sizeScale": "linear",
            "strokeColorField": None,
            "strokeColorScale": "quantile",
            "heightField": {
              "name": "std_pop_general",
              "type": "string"
            },
            "heightScale": "point",
            "radiusField": None,
            "radiusScale": "linear"
          }
        },
        {
          "id": "xnhtuh",
          "type": "geojson",
          "config": {
            "dataId": "fb_stats",
            "label": "fb_stats_youth",
            "color": [
              130,
              154,
              227
            ],
            "columns": {
              "geojson": "geometry"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 0.8,
              "strokeOpacity": 0.8,
              "thickness": 0.5,
              "strokeColor": None,
              "colorRange": {
                "name": "ColorBrewer RdYlGn-11",
                "type": "diverging",
                "category": "ColorBrewer",
                "colors": [
                  "#006837",
                  "#1a9850",
                  "#66bd63",
                  "#a6d96a",
                  "#d9ef8b",
                  "#ffffbf",
                  "#fee08b",
                  "#fdae61",
                  "#f46d43",
                  "#d73027",
                  "#a50026"
                ],
                "reversed": True
              },
              "strokeColorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "radius": 10,
              "sizeRange": [
                0,
                10
              ],
              "radiusRange": [
                0,
                50
              ],
              "heightRange": [
                0,
                500
              ],
              "elevationScale": 5,
              "stroked": True,
              "filled": True,
              "enable3d": False,
              "wireframe": False
            },
            "hidden": False,
            "textLabel": [
              {
                "field": None,
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 18,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center"
              }
            ]
          },
          "visualChannels": {
            "colorField": {
              "name": "sum_pop_youth",
              "type": "real"
            },
            "colorScale": "quantile",
            "sizeField": None,
            "sizeScale": "linear",
            "strokeColorField": None,
            "strokeColorScale": "quantile",
            "heightField": {
              "name": "std_pop_youth",
              "type": "string"
            },
            "heightScale": "point",
            "radiusField": None,
            "radiusScale": "linear"
          }
        }
      ],
      "interactionConfig": {
        "tooltip": {
          "fieldsToShow": {
            "fb_stats": [
              {
                "name": "vor_id",
                "format": None
              },
              {
                "name": "sum_pop_general",
                "format": None
              },
              {
                "name": "std_pop_general",
                "format": None
              },
              {
                "name": "sum_pop_youth",
                "format": None
              },
              {
                "name": "std_pop_youth",
                "format": None
              }
            ]
          },
          "compareMode": False,
          "compareType": "absolute",
          "enabled": True
        },
        "brush": {
          "size": 0.5,
          "enabled": False
        },
        "geocoder": {
          "enabled": False
        },
        "coordinate": {
          "enabled": False
        }
      },
      "layerBlending": "normal",
      "splitMaps": [
        {
          "layers": {
            "ie5oopl": True,
            "xnhtuh": False
          }
        },
        {
          "layers": {
            "ie5oopl": False,
            "xnhtuh": True
          }
        }
      ],
      "animationConfig": {
        "currentTime": None,
        "speed": 1
      }
    },
    "mapState": {
      "bearing": 0,
      "dragRotate": False,
      "latitude": 31.51831651933876,
      "longitude": 74.2374154666666,
      "pitch": 0,
      "zoom": 10.064621170547618,
      "isSplit": True
    },
    "mapStyle": {
      "styleType": "dark",
      "topLayerGroups": {},
      "visibleLayerGroups": {
        "label": True,
        "road": True,
        "border": False,
        "building": True,
        "water": True,
        "land": True,
        "3d building": False
      },
      "threeDBuildingColor": [
        9.665468314072013,
        17.18305478057247,
        31.1442867897876
      ],
      "mapStyles": {}
    }
  }
}




lahore_vor_poi_test = {
  "version": "v1",
  "config": {
    "visState": {
      "filters": [],
      "layers": [
        {
          "id": "u9hn0a",
          "type": "point",
          "config": {
            "dataId": "poi",
            "label": "poi",
            "color": [
              221,
              178,
              124
            ],
            "columns": {
              "lat": "lat",
              "lng": "lon",
              "altitude": None
            },
            "isVisible": True,
            "visConfig": {
              "radius": 10,
              "fixedRadius": False,
              "opacity": 0.8,
              "outline": False,
              "thickness": 2,
              "strokeColor": None,
              "colorRange": {
                "name": "Uber Viz Qualitative 4",
                "type": "qualitative",
                "category": "Uber",
                "colors": [
                  "#12939A",
                  "#DDB27C",
                  "#88572C",
                  "#FF991F",
                  "#F15C17",
                  "#223F9A",
                  "#DA70BF",
                  "#125C77",
                  "#4DC19C",
                  "#776E57",
                  "#17B8BE",
                  "#F6D18A",
                  "#B7885E",
                  "#FFCB99",
                  "#F89570",
                  "#829AE3",
                  "#E79FD5",
                  "#1E96BE",
                  "#89DAC1",
                  "#B3AD9E"
                ]
              },
              "strokeColorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "radiusRange": [
                0,
                50
              ],
              "filled": True
            },
            "hidden": False,
            "textLabel": [
              {
                "field": None,
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 18,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center"
              }
            ]
          },
          "visualChannels": {
            "colorField": {
              "name": "second_type",
              "type": "string"
            },
            "colorScale": "ordinal",
            "strokeColorField": None,
            "strokeColorScale": "quantile",
            "sizeField": None,
            "sizeScale": "linear"
          }
        },
        {
          "id": "bdpnk4p",
          "type": "geojson",
          "config": {
            "dataId": "vors",
            "label": "vor",
            "color": [
              18,
              147,
              154
            ],
            "columns": {
              "geojson": "geometry"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 0.8,
              "strokeOpacity": 0.8,
              "thickness": 0.5,
              "strokeColor": [
                242,
                108,
                0
              ],
              "colorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "strokeColorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "radius": 10,
              "sizeRange": [
                0,
                10
              ],
              "radiusRange": [
                0,
                50
              ],
              "heightRange": [
                0,
                500
              ],
              "elevationScale": 5,
              "stroked": True,
              "filled": False,
              "enable3d": False,
              "wireframe": False
            },
            "hidden": False,
            "textLabel": [
              {
                "field": None,
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 18,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center"
              }
            ]
          },
          "visualChannels": {
            "colorField": None,
            "colorScale": "quantile",
            "sizeField": None,
            "sizeScale": "linear",
            "strokeColorField": None,
            "strokeColorScale": "quantile",
            "heightField": None,
            "heightScale": "linear",
            "radiusField": None,
            "radiusScale": "linear"
          }
        },
        {
          "id": "x55i4uj",
          "type": "geojson",
          "config": {
            "dataId": "centroids",
            "label": "new layer",
            "color": [
              255,
              203,
              153
            ],
            "columns": {
              "geojson": "geometry"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 0.8,
              "strokeOpacity": 0.8,
              "thickness": 0.5,
              "strokeColor": [
                253,
                121,
                0
              ],
              "colorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "strokeColorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "radius": 15,
              "sizeRange": [
                0,
                10
              ],
              "radiusRange": [
                0,
                50
              ],
              "heightRange": [
                0,
                500
              ],
              "elevationScale": 5,
              "stroked": True,
              "filled": False,
              "enable3d": False,
              "wireframe": False
            },
            "hidden": False,
            "textLabel": [
              {
                "field": None,
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 18,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center"
              }
            ]
          },
          "visualChannels": {
            "colorField": None,
            "colorScale": "quantile",
            "sizeField": None,
            "sizeScale": "linear",
            "strokeColorField": None,
            "strokeColorScale": "quantile",
            "heightField": None,
            "heightScale": "linear",
            "radiusField": None,
            "radiusScale": "linear"
          }
        }
      ],
      "interactionConfig": {
        "tooltip": {
          "fieldsToShow": {
            "poi": [
              {
                "name": "place_id",
                "format": None
              },
              {
                "name": "name",
                "format": None
              },
              {
                "name": "user_ratings_total",
                "format": None
              },
              {
                "name": "first_type",
                "format": None
              },
              {
                "name": "second_type",
                "format": None
              }
            ],
            "centroids": [
              {
                "name": "vor_id",
                "format": None
              },
              {
                "name": "area_sq",
                "format": None
              },
              {
                "name": "area_sqrt",
                "format": None
              },
              {
                "name": "sum_pop",
                "format": None
              },
              {
                "name": "mean_pop",
                "format": None
              }
            ],
            "vors": [
              {
                "name": "vor_id",
                "format": None
              },
              {
                "name": "area_sq",
                "format": None
              },
              {
                "name": "area_sqrt",
                "format": None
              },
              {
                "name": "sum_pop",
                "format": None
              },
              {
                "name": "mean_pop",
                "format": None
              }
            ]
          },
          "compareMode": False,
          "compareType": "absolute",
          "enabled": True
        },
        "brush": {
          "size": 0.5,
          "enabled": False
        },
        "geocoder": {
          "enabled": False
        },
        "coordinate": {
          "enabled": False
        }
      },
      "layerBlending": "normal",
      "splitMaps": [],
      "animationConfig": {
        "currentTime": None,
        "speed": 1
      }
    },
    "mapState": {
      "bearing": 0,
      "dragRotate": False,
      "latitude": 31.531559105891255,
      "longitude": 74.30966178845453,
      "pitch": 0,
      "zoom": 11.241820548597422,
      "isSplit": False
    },
    "mapStyle": {
      "styleType": "dark",
      "topLayerGroups": {},
      "visibleLayerGroups": {
        "label": True,
        "road": True,
        "border": False,
        "building": True,
        "water": True,
        "land": True,
        "3d building": False
      },
      "threeDBuildingColor": [
        9.665468314072013,
        17.18305478057247,
        31.1442867897876
      ],
      "mapStyles": {}
    }
  }
}




lahore_pop_grid = {
  "version": "v1",
  "config": {
    "visState": {
      "filters": [],
      "layers": [
        {
          "id": "2wep73",
          "type": "geojson",
          "config": {
            "dataId": "lahore_pop",
            "label": "lahore_pop",
            "color": [
              18,
              147,
              154
            ],
            "columns": {
              "geojson": "geometry"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 0.47,
              "strokeOpacity": 0.8,
              "thickness": 0,
              "strokeColor": [
                255,
                254,
                230
              ],
              "colorRange": {
                "name": "ColorBrewer RdYlGn-11",
                "type": "diverging",
                "category": "ColorBrewer",
                "colors": [
                  "#006837",
                  "#1a9850",
                  "#66bd63",
                  "#a6d96a",
                  "#d9ef8b",
                  "#ffffbf",
                  "#fee08b",
                  "#fdae61",
                  "#f46d43",
                  "#d73027",
                  "#a50026"
                ],
                "reversed": True
              },
              "strokeColorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "radius": 10,
              "sizeRange": [
                0,
                10
              ],
              "radiusRange": [
                0,
                50
              ],
              "heightRange": [
                0,
                500
              ],
              "elevationScale": 5,
              "stroked": True,
              "filled": True,
              "enable3d": False,
              "wireframe": False
            },
            "hidden": False,
            "textLabel": [
              {
                "field": None,
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 18,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center"
              }
            ]
          },
          "visualChannels": {
            "colorField": {
              "name": "sum_pop",
              "type": "real"
            },
            "colorScale": "quantile",
            "sizeField": None,
            "sizeScale": "linear",
            "strokeColorField": None,
            "strokeColorScale": "quantile",
            "heightField": None,
            "heightScale": "linear",
            "radiusField": None,
            "radiusScale": "linear"
          }
        }
      ],
      "interactionConfig": {
        "tooltip": {
          "fieldsToShow": {
            "lahore_pop": [
              {
                "name": "vor_id",
                "format": None
              },
              {
                "name": "area_sq",
                "format": None
              },
              {
                "name": "area_sqrt",
                "format": None
              },
              {
                "name": "sum_pop",
                "format": None
              },
              {
                "name": "mean_pop",
                "format": None
              }
            ]
          },
          "compareMode": False,
          "compareType": "absolute",
          "enabled": True
        },
        "brush": {
          "size": 0.5,
          "enabled": False
        },
        "geocoder": {
          "enabled": False
        },
        "coordinate": {
          "enabled": False
        }
      },
      "layerBlending": "normal",
      "splitMaps": [],
      "animationConfig": {
        "currentTime": None,
        "speed": 1
      }
    },
    "mapState": {
      "bearing": 0,
      "dragRotate": False,
      "latitude": 31.459637707068264,
      "longitude": 74.32639973443413,
      "pitch": 0,
      "zoom": 9.878952432297172,
      "isSplit": False
    },
    "mapStyle": {
      "styleType": "light",
      "topLayerGroups": {},
      "visibleLayerGroups": {
        "label": True,
        "road": True,
        "border": True,
        "building": True,
        "water": True,
        "land": True,
        "3d building": False
      },
      "threeDBuildingColor": [
        218.82023004728686,
        223.47597962276103,
        223.47597962276103
      ],
      "mapStyles": {}
    }
  }
}

lahore_poi = {
  "version": "v1",
  "config": {
    "visState": {
      "filters": [],
      "layers": [
        {
          "id": "hijc7o9",
          "type": "geojson",
          "config": {
            "dataId": "polys",
            "label": "polys",
            "color": [
              210,
              0,
              0
            ],
            "columns": {
              "geojson": "geometry"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 0.17,
              "strokeOpacity": 0.8,
              "thickness": 0.5,
              "strokeColor": [
                221,
                178,
                124
              ],
              "colorRange": {
                "name": "Uber Viz Qualitative 4",
                "type": "qualitative",
                "category": "Uber",
                "colors": [
                  "#12939A",
                  "#DDB27C",
                  "#88572C",
                  "#FF991F",
                  "#F15C17",
                  "#223F9A",
                  "#DA70BF",
                  "#125C77",
                  "#4DC19C",
                  "#776E57",
                  "#17B8BE",
                  "#F6D18A",
                  "#B7885E",
                  "#FFCB99",
                  "#F89570",
                  "#829AE3",
                  "#E79FD5",
                  "#1E96BE",
                  "#89DAC1",
                  "#B3AD9E"
                ]
              },
              "strokeColorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "radius": 10,
              "sizeRange": [
                0,
                10
              ],
              "radiusRange": [
                0,
                50
              ],
              "heightRange": [
                0,
                500
              ],
              "elevationScale": 5,
              "stroked": False,
              "filled": True,
              "enable3d": False,
              "wireframe": False
            },
            "hidden": False,
            "textLabel": [
              {
                "field": None,
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 18,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center"
              }
            ]
          },
          "visualChannels": {
            "colorField": {
              "name": "amenity",
              "type": "string"
            },
            "colorScale": "ordinal",
            "sizeField": None,
            "sizeScale": "linear",
            "strokeColorField": None,
            "strokeColorScale": "quantile",
            "heightField": None,
            "heightScale": "linear",
            "radiusField": None,
            "radiusScale": "linear"
          }
        },
        {
          "id": "nlpwca9",
          "type": "geojson",
          "config": {
            "dataId": "point",
            "label": "points",
            "color": [
              210,
              0,
              0
            ],
            "columns": {
              "geojson": "geometry"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 0.8,
              "strokeOpacity": 0.8,
              "thickness": 0.5,
              "strokeColor": None,
              "colorRange": {
                "name": "Uber Viz Qualitative 4",
                "type": "qualitative",
                "category": "Uber",
                "colors": [
                  "#12939A",
                  "#DDB27C",
                  "#88572C",
                  "#FF991F",
                  "#F15C17",
                  "#223F9A",
                  "#DA70BF",
                  "#125C77",
                  "#4DC19C",
                  "#776E57",
                  "#17B8BE",
                  "#F6D18A",
                  "#B7885E",
                  "#FFCB99",
                  "#F89570",
                  "#829AE3",
                  "#E79FD5",
                  "#1E96BE",
                  "#89DAC1",
                  "#B3AD9E"
                ]
              },
              "strokeColorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "radius": 10,
              "sizeRange": [
                0,
                10
              ],
              "radiusRange": [
                0,
                50
              ],
              "heightRange": [
                0,
                500
              ],
              "elevationScale": 5,
              "stroked": False,
              "filled": True,
              "enable3d": False,
              "wireframe": False
            },
            "hidden": False,
            "textLabel": [
              {
                "field": None,
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 18,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center"
              }
            ]
          },
          "visualChannels": {
            "colorField": {
              "name": "amenity",
              "type": "string"
            },
            "colorScale": "ordinal",
            "sizeField": None,
            "sizeScale": "linear",
            "strokeColorField": None,
            "strokeColorScale": "quantile",
            "heightField": None,
            "heightScale": "linear",
            "radiusField": None,
            "radiusScale": "linear"
          }
        },
        {
          "id": "8mt9uw",
          "type": "geojson",
          "config": {
            "dataId": "boundary",
            "label": "new layer",
            "color": [
              255,
              153,
              31
            ],
            "columns": {
              "geojson": "geometry"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 0.8,
              "strokeOpacity": 0.8,
              "thickness": 2.1,
              "strokeColor": [
                254,
                242,
                26
              ],
              "colorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "strokeColorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "radius": 10,
              "sizeRange": [
                0,
                10
              ],
              "radiusRange": [
                0,
                50
              ],
              "heightRange": [
                0,
                500
              ],
              "elevationScale": 5,
              "stroked": True,
              "filled": False,
              "enable3d": False,
              "wireframe": False
            },
            "hidden": False,
            "textLabel": [
              {
                "field": None,
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 18,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center"
              }
            ]
          },
          "visualChannels": {
            "colorField": None,
            "colorScale": "quantile",
            "sizeField": None,
            "sizeScale": "linear",
            "strokeColorField": None,
            "strokeColorScale": "quantile",
            "heightField": None,
            "heightScale": "linear",
            "radiusField": None,
            "radiusScale": "linear"
          }
        }
      ],
      "interactionConfig": {
        "tooltip": {
          "fieldsToShow": {
            "polys": [
              {
                "name": "id",
                "format": None
              },
              {
                "name": "amenity",
                "format": None
              }
            ],
            "point": [
              {
                "name": "id",
                "format": None
              },
              {
                "name": "amenity",
                "format": None
              }
            ],
            "boundary": [
              {
                "name": "OBJECTID",
                "format": None
              },
              {
                "name": "PROVINCE",
                "format": None
              },
              {
                "name": "DISTRICT",
                "format": None
              },
              {
                "name": "Shape_Leng",
                "format": None
              },
              {
                "name": "ADMIN_UNIT",
                "format": None
              }
            ]
          },
          "compareMode": False,
          "compareType": "absolute",
          "enabled": True
        },
        "brush": {
          "size": 0.5,
          "enabled": False
        },
        "geocoder": {
          "enabled": False
        },
        "coordinate": {
          "enabled": False
        }
      },
      "layerBlending": "normal",
      "splitMaps": [],
      "animationConfig": {
        "currentTime": None,
        "speed": 1
      }
    },
    "mapState": {
      "bearing": 0,
      "dragRotate": False,
      "latitude": 31.48253728148019,
      "longitude": 74.35773864395924,
      "pitch": 0,
      "zoom": 9.87076704893623,
      "isSplit": False
    },
    "mapStyle": {
      "styleType": "dark",
      "topLayerGroups": {},
      "visibleLayerGroups": {
        "label": True,
        "road": True,
        "border": False,
        "building": True,
        "water": True,
        "land": True,
        "3d building": False
      },
      "threeDBuildingColor": [
        9.665468314072013,
        17.18305478057247,
        31.1442867897876
      ],
      "mapStyles": {}
    }
  }
}