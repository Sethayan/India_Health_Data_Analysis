function ShowStateView(stateStats, comparisonData) {
    const infraCtx = document.getElementById('stateInfraChart');
    if (infraCtx) {
        new Chart(infraCtx, {
            type: 'bar',
            data: {
                labels: ['Sub Centres', 'PHCs', 'CHCs'],
                datasets: [
                    {
                        label: 'Rural',
                        data: [
                            stateStats.sub_centres_rural,
                            stateStats.phcs_rural,
                            stateStats.chcs_rural
                        ],
                        backgroundColor: 'rgba(25, 135, 84, 0.8)',
                        borderRadius: 4
                    },
                    {
                        label: 'Urban',
                        data: [
                            stateStats.sub_centres_urban,
                            stateStats.phcs_urban,
                            stateStats.chcs_urban
                        ],
                        backgroundColor: 'rgba(13, 110, 253, 0.8)',
                        borderRadius: 4
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'top',
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
                        backgroundColor: 'rgba(0, 0, 0, 0.8)',
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

    const popCtx = document.getElementById('populationChart');
    if (popCtx) {
        new Chart(popCtx, {
            type: 'pie',
            data: {
                labels: ['Rural Population', 'Urban Population'],
                datasets: [{
                    data: [stateStats.population_rural, stateStats.population_urban],
                    backgroundColor: ['rgba(25, 135, 84, 0.8)', 'rgba(220, 53, 69, 0.8)'],
                    borderWidth: 0
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { position: 'bottom' }
                }
            }
        });
    }

    const vitalCtx = document.getElementById('vitalStatsChart');
    if (vitalCtx) {
        new Chart(vitalCtx, {
            type: 'bar',
            data: {
                labels: ['Birth Rate', 'Death Rate'],
                datasets: [{
                    label: 'Rate per 1000',
                    data: [stateStats.birth_rate, stateStats.death_rate],
                    backgroundColor: ['rgba(25, 135, 84, 0.8)', 'rgba(220, 53, 69, 0.8)'],
                    borderRadius: 4
                }]
            },
            options: {
                plugins: {
                    legend: {
                        display: false,
                        position: 'top',
                        labels: {
                            usePointStyle: true,
                            padding: 15,
                            font: {
                                family: "'Inter', sans-serif",
                                size: 12
                            }
                        },
                        tooltip: {
                            backgroundColor: 'rgba(0, 0, 0, 0.8)',
                            titleFont: { family: "'Inter', sans-serif", size: 13 },
                            bodyFont: { family: "'Inter', sans-serif", size: 12 },
                            padding: 12,
                            cornerRadius: 8
                        }
                    },
                    tooltip: {
                        backgroundColor: 'rgba(0, 0, 0, 0.8)',
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
    if (comparisonData) {
        const compCtx = document.getElementById('comparisonChart');
        if (compCtx) {
            new Chart(compCtx, {
                type: 'bar',
                data: {
                    labels: ['Sub Centres', 'PHCs', 'CHCs'],
                    datasets: [
                        {
                            label: '2005',
                            data: [comparisonData.sc_2005, comparisonData.phc_2005, comparisonData.chc_2005],
                            backgroundColor: 'rgba(13, 110, 253, 0.2)',
                            borderColor: 'rgba(13, 110, 253, 0.8)',
                            borderWidth: 2
                        },
                        {
                            label: '2023',
                            data: [comparisonData.sc_2023, comparisonData.phc_2023, comparisonData.chc_2023],
                            backgroundColor: 'rgba(25, 135, 84, 0.2)',
                            borderColor: 'rgba(25, 135, 84, 0.8)',
                            borderWidth: 2
                        }
                    ]
                },
                options: {
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            position: 'top',
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
                            backgroundColor: 'rgba(0, 0, 0, 0.8)',
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
}