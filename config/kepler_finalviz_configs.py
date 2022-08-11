islamabad_config = {
  "version": "v1",
  "config": {
    "visState": {
      "filters": [],
      "layers": [
        {
          "id": "9uuvgxr",
          "type": "geojson",
          "config": {
            "dataId": "value",
            "label": "value",
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
              "opacity": 0.4,
              "strokeOpacity": 1,
              "thickness": 0.1,
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
                  "#a50026",
                  "#d73027",
                  "#f46d43",
                  "#fdae61",
                  "#fee08b",
                  "#ffffbf",
                  "#d9ef8b",
                  "#a6d96a",
                  "#66bd63",
                  "#1a9850",
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
              "name": "value",
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
            "value": [
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
                "name": "value",
                "format": None
              },
              {
                "name": "million_pkr",
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
      "latitude": 33.668044103304155,
      "longitude": 73.12067374096367,
      "pitch": 0,
      "zoom": 10.326613285230815,
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
        3.7245996603793508,
        6.518049405663864,
        13.036098811327728
      ],
      "mapStyles": {}
    }
  }
}

lahore_config = {
  "version": "v1",
  "config": {
    "visState": {
      "filters": [],
      "layers": [
        {
          "id": "9uuvgxr",
          "type": "geojson",
          "config": {
            "dataId": "value",
            "label": "value",
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
              "opacity": 0.4,
              "strokeOpacity": 0.8,
              "thickness": 0.5,
              "strokeColor": [
                221,
                178,
                124
              ],
              "colorRange": {
                "name": "ColorBrewer RdYlGn-11",
                "type": "diverging",
                "category": "ColorBrewer",
                "colors": [
                  "#a50026",
                  "#d73027",
                  "#f46d43",
                  "#fdae61",
                  "#fee08b",
                  "#ffffbf",
                  "#d9ef8b",
                  "#a6d96a",
                  "#66bd63",
                  "#1a9850",
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
              "name": "value",
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
            "value": [
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
                "name": "value",
                "format": None
              },
              {
                "name": "million_pkr",
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
      "latitude": 31.47942034630996,
      "longitude": 74.32528884318047,
      "pitch": 0,
      "zoom": 9.79430269995701,
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
        3.7245996603793508,
        6.518049405663864,
        13.036098811327728
      ],
      "mapStyles": {}
    }
  }
}

karachi_config = {
  "version": "v1",
  "config": {
    "visState": {
      "filters": [],
      "layers": [
        {
          "id": "9uuvgxr",
          "type": "geojson",
          "config": {
            "dataId": "value",
            "label": "value",
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
              "opacity": 0.4,
              "strokeOpacity": 0.8,
              "thickness": 0.5,
              "strokeColor": [
                221,
                178,
                124
              ],
              "colorRange": {
                "name": "ColorBrewer RdYlGn-11",
                "type": "diverging",
                "category": "ColorBrewer",
                "colors": [
                  "#a50026",
                  "#d73027",
                  "#f46d43",
                  "#fdae61",
                  "#fee08b",
                  "#ffffbf",
                  "#d9ef8b",
                  "#a6d96a",
                  "#66bd63",
                  "#1a9850",
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
              "name": "value",
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
            "value": [
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
                "name": "value",
                "format": None
              },
              {
                "name": "million_pkr",
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
      "latitude": 25.09846150259658,
      "longitude": 67.11359160640941,
      "pitch": 0,
      "zoom": 8.991673644092604,
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
        3.7245996603793508,
        6.518049405663864,
        13.036098811327728
      ],
      "mapStyles": {}
    }
  }
}