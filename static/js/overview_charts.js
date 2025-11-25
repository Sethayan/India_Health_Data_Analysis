function CreateDashboardCharts(shortfallData, nationalStats) {
    if (shortfallData && shortfallData.labels) {
        const shortfallChart = document.getElementById('shortfallChart');
        if (shortfallChart) {
            // Need to only show states which has shortfall greater than 0
            const filteredData = {
                labels: [],
                sc: [],
                phc: [],
                chc: []
            };

            // Need to filter this data as there exists rows where shortfall is 0 and
            // space is limited for the graph with high number of states
            for (let i = 0; i < shortfallData.labels.length; i++) {
                if (shortfallData.phc_shortfall[i] > 0 ||
                    shortfallData.chc_shortfall[i] > 0 ||
                    shortfallData.sc_shortfall[i] > 0) {
                    filteredData.labels.push(shortfallData.labels[i]);
                    filteredData.sc.push(shortfallData.sc_shortfall[i]);
                    filteredData.phc.push(shortfallData.phc_shortfall[i]);
                    filteredData.chc.push(shortfallData.chc_shortfall[i]);
                }
            }

            new Chart(shortfallChart, {
                type: 'bar',
                data: {
                    labels: filteredData.labels,
                    datasets: [
                        {
                            label: 'Sub Centres',
                            data: filteredData.sc,
                            backgroundColor: 'rgba(201, 50, 65, 0.2)',
                            borderColor: 'rgba(220, 42, 60, 0.8)',
                            borderWidth: 1
                        },
                        {
                            label: 'PHCs',
                            data: filteredData.phc,
                            backgroundColor: 'rgba(255, 193, 7, 0.2)',
                            borderColor: 'rgba(253, 196, 26, 0.8)',
                            borderWidth: 1
                        },
                        {
                            label: 'CHCs',
                            data: filteredData.chc,
                            backgroundColor: 'rgba(24, 203, 239, 0.2)',
                            borderColor: 'rgba(13, 202, 240, 0.8)',
                            borderWidth: 1
                        }
                    ]
                },
                options: {
                    plugins: {
                        legend: {
                            position: 'bottom',
                            labels: {
                                usePointStyle: true,
                                padding: 15,
                                font: {
                                    family: "'Inter', sans-serif",
                                    size: 12
                                }
                            }
                        },
                        tooltip: {
                            backgroundColor: 'rgba(4, 4, 4, 0.8)',
                            titleFont: { family: "'Inter', sans-serif", size: 13 },
                            bodyFont: { family: "'Inter', sans-serif", size: 12 },
                            padding: 12,
                            cornerRadius: 8
                        }
                    },
                    scales: {
                        x: {
                            grid: { display: false },
                            ticks: {
                                font: { family: "'Inter', sans-serif", size: 11 },
                                maxRotation: 45,
                                minRotation: 45
                            }
                        },
                        y: {
                            grid: { color: 'rgba(8, 7, 7, 0.05)' },
                            title: {
                                display: true,
                                text: 'Shortfall %',
                                font: { family: "'Inter', sans-serif", size: 11 }
                            }
                        }
                    }
                }
            });
        }
    }

    const ruralUrbanCtx = document.getElementById('ruralUrbanChart');
    if (ruralUrbanCtx && nationalStats) {
        new Chart(ruralUrbanCtx, {
            type: 'doughnut',
            data: {
                labels: ['Rural Sub Centres', 'Urban Sub Centres', 'Rural PHCs', 'Urban PHCs', 'Rural CHCs', 'Urban CHCs'],
                datasets: [{
                    data: [
                        nationalStats.rural_sub_centres,
                        nationalStats.urban_sub_centres,
                        nationalStats.rural_phcs,
                        nationalStats.urban_phcs,
                        nationalStats.rural_chcs,
                        nationalStats.urban_chcs
                    ],
                    backgroundColor: [
                        'rgba(31, 116, 244, 0.8)',
                        'rgba(12, 90, 208, 0.2)',
                        'rgba(36, 156, 100, 0.8)',
                        'rgba(12, 134, 77, 0.2)',
                        'rgba(14, 162, 192, 0.8)',
                        'rgba(23, 142, 165, 0.2)'
                    ],
                    borderWidth: 0
                }]
            },
            options: {
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'right',
                        labels: {
                            usePointStyle: true,
                            padding: 10,
                            font: { size: 11 }
                        }
                    }
                }
            }
        });
    }

    const facilityCanva = document.getElementById('facilityDistributionChart');
    if (facilityCanva && nationalStats) {
        new Chart(facilityCanva, {
            type: 'bar',
            data: {
                labels: ['Sub Centres', 'PHCs', 'CHCs', 'SDH', 'DH', 'Medical Colleges'],
                datasets: [{
                    label: 'Count',
                    data: [
                        nationalStats.total_sub_centres,
                        nationalStats.total_phcs,
                        nationalStats.total_chcs,
                        nationalStats.total_sdh,
                        nationalStats.total_dh,
                        nationalStats.total_medical_colleges
                    ],
                    backgroundColor: [
                        'rgba(41, 83, 146, 0.8)',
                        'rgba(25, 135, 84, 0.8)',
                        'rgba(9, 183, 218, 0.8)',
                        'rgba(247, 198, 50, 0.8)',
                        'rgba(227, 23, 44, 0.8)',
                        'rgba(121, 68, 220, 1)'
                    ],
                    borderRadius: 4
                }]
            },
            options: {
                indexAxis: 'y',  // For horizontal bar chart. Courtsey: https://www.chartjs.org/docs/latest/samples/bar/horizontal.html
                plugins: {
                    tooltip: {
                        backgroundColor: 'rgba(0, 0, 0, 0.8)',
                        titleFont: { family: "'Inter', sans-serif", size: 13 },
                        bodyFont: { family: "'Inter', sans-serif", size: 12 },
                        padding: 12,
                        cornerRadius: 8
                    },
                    legend: { display: false }
                },
                scales: {
                    x: {
                        grid: { display: false },
                        ticks: {
                            font: { family: "'Inter', sans-serif", size: 11 }
                        }
                    },
                    y: {
                        grid: { color: 'rgba(0, 0, 0, 0.05)' },
                        ticks: {
                            font: { family: "'Inter', sans-serif", size: 11 }
                        }
                    }
                }
            }
        });
    }
}

async function loadShortfallHeatMap(shortfallData) {

    const filteredData = {
        labels: [],
        sc: [],
        phc: [],
        chc: []
    };

    // Need to filter this data as there exists rows where shortfall is 0 and
    // space is limited for the graph with high number of states
    for (let i = 0; i < shortfallData.labels.length; i++) {
        if (shortfallData.phc_shortfall[i] > 0 ||
            shortfallData.chc_shortfall[i] > 0 ||
            shortfallData.sc_shortfall[i] > 0) {
            filteredData.labels.push(shortfallData.labels[i]);
            filteredData.sc.push(shortfallData.sc_shortfall[i]);
            filteredData.phc.push(shortfallData.phc_shortfall[i]);
            filteredData.chc.push(shortfallData.chc_shortfall[i]);
        }
    }

    document.getElementById("loader").style.display = "flex";

    const geojsonUrl = "static/geoJSON/india.geojson";
    const geoJsonStateProp = "st_nm";

    const container = d3.select("#map");
    const bbox = container.node().getBoundingClientRect();
    const width = Math.max(700, bbox.width);
    const height = Math.max(600, window.innerHeight * 0.9);

    const svg = container.append("svg")
        .attr("viewBox", `0 0 ${width} ${height}`)
        .attr("preserveAspectRatio", "xMidYMid meet")
        .style("width", "100%")
        .style("height", "100%");

    const tooltip = d3.select("#map-tooltip");

    // Using mercaptor project with center of india as 82 E, 23 N
    const projection = d3.geoMercator()
        .center([82, 23])
        .scale(1100)
        .translate([width / 2, height / 2]);

    const [geojson] = await Promise.all([
        d3.json(geojsonUrl)
    ]);


    const path = d3.geoPath().projection(projection);
    const valueByState = new Map();
    for (let i = 0; i < filteredData.labels.length; i++) {
        const state = filteredData.labels[i];
        const val = (filteredData.sc[i] + filteredData.phc[i] + filteredData.chc[i])/3;
        valueByState.set(state, val);
    }

    const values = Array.from(valueByState.values()).filter(v => v !== null && v !== undefined);
    const minVal = d3.min(values);
    const maxVal = d3.max(values);

    const color = d3.scaleSequential()
        .domain([minVal, maxVal])
        .interpolator(d3.interpolateYlOrRd);

    projection.fitSize([width, height], geojson);

    svg.append("g")
        .selectAll("path")
        .data(geojson.features)
        .join("path")
        .attr("class", "state")
        .attr("d", path)
        .attr("fill", d => {
            const stateName = (d.properties[geoJsonStateProp] || "").trim();
            const v = valueByState.get(stateName);
            return (v == null) ? "#eee" : color(v);
        })
        .on("mousemove", (event, d) => {
            const stateName = (d.properties[geoJsonStateProp] || "").trim();
            const v = valueByState.get(stateName);
            tooltip.style("display", "block")
                .style("left", (event.clientX + 12) + "px")
                .style("top", (event.clientY + 12) + "px")
                .html(`<strong>${stateName}</strong><br/>
                    SC Shortfall: ${filteredData.sc[filteredData.labels.indexOf(stateName)] || 0} %<br/>
                    PHC Shortfall: ${filteredData.phc[filteredData.labels.indexOf(stateName)] || 0} %<br/>
                    CHC Shortfall: ${filteredData.chc[filteredData.labels.indexOf(stateName)] || 0} %`);
        })
        .on("mouseleave", () => tooltip.style("display", "none"))
        .on("click", (event, d) => {
            const stateName = (d.properties[geoJsonStateProp] || "").trim();
            console.log(stateName + " Clicked");
        });

    const legendWidth = 300, legendHeight = 10;
    const legend = svg.append("g")
        .attr("class", "legend")
        .attr("transform", `translate(${20}, ${height - 50})`);

    const defs = svg.append("defs");
    const gradId = "legend-gradient";
    const gradient = defs.append("linearGradient").attr("id", gradId).attr("x1", "0%").attr("x2", "100%");

    const stops = 10;
    d3.range(stops + 1).forEach(i => {
        gradient.append("stop")
            .attr("offset", `${(i / stops) * 100}%`)
            .attr("stop-color", color(minVal + (i / stops) * (maxVal - minVal)));
    });

    legend.append("rect")
        .attr("width", legendWidth)
        .attr("height", legendHeight)
        .style("fill", `url(#${gradId})`);

    const tickValues = d3.scaleLinear().domain([minVal, maxVal]).ticks(5);
    const x = d3.scaleLinear().domain([minVal, maxVal]).range([0, legendWidth]);
    legend.append("g")
        .attr("transform", `translate(0, ${legendHeight})`)
        .call(d3.axisBottom(x).tickValues(tickValues).tickFormat(d3.format(".2s")));

    legend.append("text")
        .attr("x", 0)
        .attr("y", -6)
        .text("Shortfall %")
        .style("font-size", "12px");

    window.addEventListener("resize", () => {
        const newW = Math.max(700, container.node().getBoundingClientRect().width);
        const newH = Math.max(600, window.innerHeight * 0.9);
        svg.attr("width", newW).attr("height", newH);
        projection.translate([newW / 2, newH / 2]);
        svg.selectAll("path").attr("d", path);
    });

    document.getElementById("loader").style.display = "none";
}