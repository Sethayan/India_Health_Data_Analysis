function initComparisonCharts(comparisonData, yearlyData) {
    if (comparisonData && comparisonData.infra_comparison) {
        const infra = comparisonData.infra_comparison;

        // SC Comparison Chart
        const scCtx = document.getElementById('scComparisonChart');
        if (scCtx) {
            new Chart(scCtx, {
                type: 'bar',
                data: {
                    labels: infra.labels.map(l => truncateLabel(l, 10)),
                    datasets: [
                        {
                            label: '2005',
                            data: infra.sc_2005,
                            backgroundColor: 'rgba(13, 110, 253, 0.2)',
                            borderColor: 'rgba(13, 110, 253, 0.8)',
                            borderWidth: 1
                        },
                        {
                            label: '2023',
                            data: infra.sc_2023,
                            backgroundColor: 'rgba(25, 135, 84, 0.2)',
                            borderColor: 'rgba(25, 135, 84, 0.8)',
                            borderWidth: 1
                        }
                    ]
                },
                options: {
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
                            ticks: { maxRotation: 45, minRotation: 45, font: { size: 9 } }
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

        // PHC Comparison Chart
        const phcCtx = document.getElementById('phcComparisonChart');
        if (phcCtx) {
            new Chart(phcCtx, {
                type: 'bar',
                data: {
                    labels: infra.labels.map(l => truncateLabel(l, 10)),
                    datasets: [
                        {
                            label: '2005',
                            data: infra.phc_2005,
                            backgroundColor: 'rgba(13, 110, 253, 0.2)',
                            borderColor: 'rgba(13, 110, 253, 0.8)',
                            borderWidth: 1
                        },
                        {
                            label: '2023',
                            data: infra.phc_2023,
                            backgroundColor: 'rgba(25, 135, 84, 0.2)',
                            borderColor: 'rgba(25, 135, 84, 0.8)',
                            borderWidth: 1
                        }
                    ]
                },
                options: {
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
                            ticks: { maxRotation: 45, minRotation: 45, font: { size: 9 } }
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

        // CHC Comparison Chart
        const chcCtx = document.getElementById('chcComparisonChart');
        if (chcCtx) {
            new Chart(chcCtx, {
                type: 'bar',
                data: {
                    labels: infra.labels.map(l => truncateLabel(l, 10)),
                    datasets: [
                        {
                            label: '2005',
                            data: infra.chc_2005,
                            backgroundColor: 'rgba(13, 110, 253, 0.2)',
                            borderColor: 'rgba(13, 110, 253, 0.8)',
                            borderWidth: 1
                        },
                        {
                            label: '2023',
                            data: infra.chc_2023,
                            backgroundColor: 'rgba(25, 135, 84, 0.2)',
                            borderColor: 'rgba(25, 135, 84, 0.8)',
                            borderWidth: 1
                        }
                    ]
                },
                options: {
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
                            ticks: { maxRotation: 45, minRotation: 45, font: { size: 9 } }
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

        // Populate table
        const tbody = $('#infraTableBody');
        tbody.empty();
        for (let i = 0; i < infra.labels.length; i++) {
            const scChange = infra.sc_2023[i] - infra.sc_2005[i];
            const phcChange = infra.phc_2023[i] - infra.phc_2005[i];
            const chcChange = infra.chc_2023[i] - infra.chc_2005[i];

            tbody.append(`
                <tr>
                    <td>${infra.labels[i]}</td>
                    <td class="text-center">${infra.sc_2005[i].toLocaleString()}</td>
                    <td class="text-center">${infra.sc_2023[i].toLocaleString()}</td>
                    <td class="text-center ${scChange >= 0 ? 'text-success' : 'text-danger'}">
                        ${scChange >= 0 ? '+' : ''}${scChange.toLocaleString()}
                    </td>
                    <td class="text-center">${infra.phc_2005[i].toLocaleString()}</td>
                    <td class="text-center">${infra.phc_2023[i].toLocaleString()}</td>
                    <td class="text-center ${phcChange >= 0 ? 'text-success' : 'text-danger'}">
                        ${phcChange >= 0 ? '+' : ''}${phcChange.toLocaleString()}
                    </td>
                    <td class="text-center">${infra.chc_2005[i].toLocaleString()}</td>
                    <td class="text-center">${infra.chc_2023[i].toLocaleString()}</td>
                    <td class="text-center ${chcChange >= 0 ? 'text-success' : 'text-danger'}">
                        ${chcChange >= 0 ? '+' : ''}${chcChange.toLocaleString()}
                    </td>
                </tr>
            `);
        }
    }

    // Doctors Comparison Chart
    if (comparisonData && comparisonData.doctors_comparison) {
        const doctors = comparisonData.doctors_comparison;
        const docCtx = document.getElementById('doctorsComparisonChart');
        if (docCtx) {
            new Chart(docCtx, {
                type: 'bar',
                data: {
                    labels: doctors.labels.map(l => truncateLabel(l, 10)),
                    datasets: [
                        {
                            label: 'In Position 2005',
                            data: doctors.position_2005,
                            backgroundColor: 'rgba(13, 110, 253, 0.2)',
                            borderColor: 'rgba(13, 110, 253, 0.8)',
                            borderWidth: 1
                        },
                        {
                            label: 'In Position 2023',
                            data: doctors.position_2023,
                            backgroundColor: 'rgba(25, 135, 84, 0.2)',
                            borderColor: 'rgba(25, 135, 84, 0.8)',
                            borderWidth: 1
                        }
                    ]
                },
                options: {
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
                            ticks: { maxRotation: 45, minRotation: 45, font: { size: 9 } }
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

    // 2022 vs 2023 Charts
    if (yearlyData && yearlyData.function_2022_2023) {
        const yearly = yearlyData.function_2022_2023;
        const ctx = document.getElementById('yearly2022Chart');
        if (ctx) {
            // Calculate totals
            const sc2022Total = yearly.sc_2022.reduce((a, b) => a + b, 0);
            const sc2023Total = yearly.sc_2023.reduce((a, b) => a + b, 0);
            const phc2022Total = yearly.phc_2022.reduce((a, b) => a + b, 0);
            const phc2023Total = yearly.phc_2023.reduce((a, b) => a + b, 0);
            const chc2022Total = yearly.chc_2022.reduce((a, b) => a + b, 0);
            const chc2023Total = yearly.chc_2023.reduce((a, b) => a + b, 0);

            new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: ['Sub Centres', 'PHCs', 'CHCs'],
                    datasets: [
                        {
                            label: 'March 2022',
                            data: [sc2022Total, phc2022Total, chc2022Total],
                            backgroundColor: 'rgba(13, 110, 253, 0.2)',
                            borderColor: 'rgba(13, 110, 253, 0.8)',
                            borderWidth: 2
                        },
                        {
                            label: 'March 2023',
                            data: [sc2023Total, phc2023Total, chc2023Total],
                            backgroundColor: 'rgba(25, 135, 84, 0.2)',
                            borderColor: 'rgba(25, 135, 84, 0.8)',
                            borderWidth: 2
                        }
                    ]
                },
                options: {
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

    if (yearlyData && yearlyData.manpower_2022_2023) {
        const mp = yearlyData.manpower_2022_2023;
        const ctx = document.getElementById('manpower2022Chart');
        if (ctx) {
            const doc2022Total = mp.doctors_2022.reduce((a, b) => a + b, 0);
            const doc2023Total = mp.doctors_2023.reduce((a, b) => a + b, 0);
            const spec2022Total = mp.specialists_2022.reduce((a, b) => a + b, 0);
            const spec2023Total = mp.specialists_2023.reduce((a, b) => a + b, 0);

            new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: ['Doctors at PHCs', 'Specialists at CHCs'],
                    datasets: [
                        {
                            label: 'March 2022',
                            data: [doc2022Total, spec2022Total],
                            backgroundColor: 'rgba(13, 110, 253, 0.2)',
                            borderColor: 'rgba(13, 110, 253, 0.8)',
                            borderWidth: 2
                        },
                        {
                            label: 'March 2023',
                            data: [doc2023Total, spec2023Total],
                            backgroundColor: 'rgba(25, 135, 84, 0.2)',
                            borderColor: 'rgba(25, 135, 84, 0.8)',
                            borderWidth: 2
                        }
                    ]
                },
                options: {
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
