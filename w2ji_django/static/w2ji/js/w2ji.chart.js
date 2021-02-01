
function fn_areachart( id ){
	var _id = id;
		
	
	var areachart, areaChartOptions = {
	        series: [{
	            name: "Website",
	            data: [31, 10, 30, 51, 42, 109, 100, 31, 40, 28, 31, 58, 30, 51, 42, 109, 100, 116]
	        }, {
	            name: "Mobile Apps",
	            data: [11, 20, 20, 32, 34, 52, 41, 11, 32, 45, 11, 75, 20, 32, 34, 52, 41, 81]
	        }, {
	            name: "Others",
	            data: [5, 30, 9, 14, 14, 32, 21, 5, 12, 25, 5, 55, 9, 14, 14, 32, 21, 65]
	        }, {
	            name: "Others1",
	            data: [15, 40, 19, 114, 114, 132, 121, 15, 112, 125, 15, 155, 19, 114, 114, 132, 121, 165]
	        }, {
	            name: "Others2",
	            data: [25, 1234, 29, 214, 214, 232, 221, 25, 212, 225, 25, 255, 29, 214, 214, 232, 21, 65]
	        }, {
	            name: "Others3",
	            data: [25, 50, 29, 214, 214, 232, 221, 25, 212, 225, 25, 255, 29, 214, 214, 232, 21, 65]
	        }
	        
	        ],
	        chart: {
	            type: "area",
	            height: 200,
	            background: "transparent",
	            stacked: true,
	            toolbar: { show: false },
	            zoom: { enabled:false }
	        },
	        
	        theme: { mode: colors.chartTheme },
	        xaxis: {
	            type: 'category',
	            categories: ["1.1", "1.2", "1.3", "1.4", "1.5", "1.6", "1.7", "1.8", "1.9", "1.10", "1.11", "1.12", "1.13", "1.14", "1.15", "1.16", "1.17", "1.8"],
	            labels: {
	                show: true,
	                trim: false,
	                minHeight: 0,
	                maxHeight: 120,
	                style: {
	                    colors: colors.mutedColor,
	                    cssClass: "text-muted",
	                    fontFamily: base.defaultFontFamily
	                }
	            },
	            axisBorder : { show: false },
	            tooltip: {
	                enabled: false,
	                offsetX: 0
	            }
	        },
	        yaxis: {
	            labels: {
	                show: true,
	                trim: false,
	                offsetX: 0,
	                minHeight: 0,
	                maxHeight: 120,
	                style: {
	                    colors: colors.mutedColor,
	                    cssClass: "text-muted",
	                    fontFamily: base.defaultFontFamily
	                },
	                
		            
	            }
	        },	        
	        markers: {
	            size: 0,
	            strokeColors: "#fff",
	            strokeWidth: 0,
	            strokeOpacity: .9,
	            strokeDashArray: 0,
	            fillOpacity: 1,
	            discrete: [],
	            shape: "circle",
	            radius: 2,
	            offsetX: 0,
	            offsetY: 0,
	            onClick: void 0,
	            onDblClick: void 0,
	            showNullDataPoints: true,
	            hover: {
	                size: void 0,
	                sizeOffset: 3
	            }
	        },
	        colors: chartColors,
	        dataLabels: { enabled: false },
	        stroke: { curve: "smooth" , lineCap: "round" , width: 0 },
	        fill: { type: "solid" },
	        legend: {
	            show: false ,
	            position: "bottom",
	            fontFamily: base.defaultFontFamily,
	            fontWeight: 400,
	            labels: {
	                colors: colors.mutedColor,
	                useSeriesColors: false
	            },
	            markers: {
	                width: 10,
	                height: 10,
	                strokeWidth: 0,
	                strokeColor: "#fff",
	                radius: 6
	            },
	            itemMargin : { horizontal: 10 , vertical: 0 },
	            onItemClick: { toggleDataSeries: true },
	            onItemHover: { highlightDataSeries: true }
	        },
	        grid: {
	            show: true,
	            borderColor: colors.borderColor,
	            strokeDashArray: 0,
	            position: "back",
	            xaxis: {
	                lines: {
	                    show: false
	                }
	            },
	            yaxis: {
	                lines: {
	                    show: true
	                }
	            },
	            row: {
	                colors: void 0,
	                opacity: .5
	            },
	            column: {
	                colors: void 0,
	                opacity: .5
	            },
	            padding: {
	                top: 0,
	                right: 20,
	                bottom: 0,
	                left: 0
	            }
	        },
	        tooltip: {
	            style: {
	                fontSize: "12px",
	                fontFamily: base.defaultFontFamily
	            }
	            
	        }
	    },
	    
	    areachartCtn = document.querySelector("#"+id);
		areachartCtn && (areachart = new ApexCharts(areachartCtn, areaChartOptions)).render();
}

