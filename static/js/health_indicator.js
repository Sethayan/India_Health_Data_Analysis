function populateHealthIndicatorChart(indicatorData) {
    if (indicatorData.imr) {
        const imr = indicatorData.imr;

        const avgIMR = (imr.reduce((sum, i) => sum + i['IMR Total'], 0) / imr.length).toFixed(1);
        $('#avgIMR').text(avgIMR);

        const sorted = [...imr].sort((a, b) => a['IMR Total'] - b['IMR Total']);
        $('#bestIMRState').text(sorted[0]['State/UT']);
        $('#bestIMRValue').text('IMR: ' + sorted[0]['IMR Total']);
        $('#worstIMRState').text(sorted[sorted.length - 1]['State/UT']);
        $('#worstIMRValue').text('IMR: ' + sorted[sorted.length - 1]['IMR Total']);

        const ctx = document.getElementById('imrChart');
        if (ctx) {
            new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: imr.map(i => truncateLabel(i['State/UT'], 10)),
                    datasets: [{
                        label: 'IMR Total',
                        data: imr.map(i => i['IMR Total']),
                        backgroundColor: imr.map(i => i['IMR Total'] > avgIMR ? 'rgba(180, 53, 69, 0.8)' : 'rgba(75, 135, 84, 0.8)'),
                        borderRadius: 4
                    }]
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
                            backgroundColor: 'rgba(34, 0, 0, 0.8)',
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
                                font: { family: "'Inter', sans-serif", size: 11, size: 9 },
                                maxRotation: 45, minRotation: 45
                            }
                        },
                        y: {
                            grid: { color: 'rgba(0, 65, 0, 0.05)' },
                            ticks: {
                                font: { family: "'Inter', sans-serif", size: 11 }
                            }
                        }
                    }
                }
            });
        }

        const ruCtx = document.getElementById('imrRuralUrbanChart');
        if (ruCtx) {
            const avgRural = (imr.reduce((sum, i) => sum + i['IMR Rural'], 0) / imr.length).toFixed(1);
            const avgUrban = (imr.reduce((sum, i) => sum + i['IMR Urban'], 0) / imr.length).toFixed(1);

            new Chart(ruCtx, {
                type: 'doughnut',
                data: {
                    labels: ['Rural IMR (Avg)', 'Urban IMR (Avg)'],
                    datasets: [{
                        data: [avgRural, avgUrban],
                        backgroundColor: ['rgba(25, 135, 100, 0.8)', 'rgba(13, 97, 253, 0.8)'],
                        borderWidth: 0
                    }]
                },
                options: {
                    maintainAspectRatio: false,
                    plugins: {
                        legend: { position: 'bottom' }
                    }
                }
            });
        }

        const tbody = $('#imrTableBody');
        tbody.empty();
        imr.forEach(i => {
            const gap = i['IMR Rural'] - i['IMR Urban'];
            const status = i['IMR Total'] <= avgIMR ?
                '<span class="badge bg-success">Good</span>' :
                '<span class="badge bg-danger">Needs Attention</span>';
            tbody.append(`
                <tr>
                    <td>${i['State/UT']}</td>
                    <td class="text-center">${i['IMR Total']}</td>
                    <td class="text-center">${i['IMR Rural']}</td>
                    <td class="text-center">${i['IMR Urban']}</td>
                    <td class="text-center">${gap}</td>
                    <td class="text-center">${status}</td>
                </tr>
            `);
        });


        if (indicatorData.birth_death) {
            const bd = indicatorData.birth_death;

            const avgBR = (bd.reduce((sum, b) => sum + b['Birth Rate Total'], 0) / bd.length).toFixed(1);
            const avgDR = (bd.reduce((sum, b) => sum + b['Death Rate Total'], 0) / bd.length).toFixed(1);

            $('#avgBirthRate').text(avgBR);
            $('#avgDeathRate').text(avgDR);

            const sortedBR = [...bd].sort((a, b) => b['Birth Rate Total'] - a['Birth Rate Total']);
            $('#highestBRState').text(sortedBR[0]['State/UT']);
            $('#highestBRValue').text('BR: ' + sortedBR[0]['Birth Rate Total']);
            $('#lowestBRState').text(sortedBR[sortedBR.length - 1]['State/UT']);
            $('#lowestBRValue').text('BR: ' + sortedBR[sortedBR.length - 1]['Birth Rate Total']);

            const compCtx = document.getElementById('birthDeathCompChart');
            if (compCtx) {
                new Chart(compCtx, {
                    type: 'line',
                    data: {
                        labels: bd.map(b => truncateLabel(b['State/UT'], 8)),
                        datasets: [
                            {
                                label: 'Birth Rate',
                                data: bd.map(b => b['Birth Rate Total']),
                                borderColor: 'rgba(25, 135, 84, 0.8)',
                                backgroundColor: 'rgba(25, 5, 84, 0.2)',
                                fill: true,
                                tension: 0.4
                            },
                            {
                                label: 'Death Rate',
                                data: bd.map(b => b['Death Rate Total']),
                                borderColor: 'rgba(123, 53, 69, 0.8)',
                                backgroundColor: 'rgba(220, 53, 69, 0.2)',
                                fill: true,
                                tension: 0.4
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
                                backgroundColor: 'rgba(0, 0, 100, 0.08)',
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
                                    font: { family: "'Inter', sans-serif", size: 9 },
                                    maxRotation: 45, minRotation: 45
                                }
                            },
                            y: {
                                grid: { color: 'rgba(0, 0, 156, 0.5)' },
                                ticks: {
                                    font: { family: "'Inter', sans-serif", size: 11 }
                                }
                            }
                        }
                    }
                });
            }

            const tbody = $('#birthDeathTableBody');
            tbody.empty();
            bd.forEach(b => {
                tbody.append(`
                <tr>
                    <td>${b['State/UT']}</td>
                    <td class="text-center">${b['Birth Rate Total']}</td>
                    <td class="text-center">${b['Birth Rate Rural']}</td>
                    <td class="text-center">${b['Birth Rate Urban']}</td>
                    <td class="text-center">${b['Death Rate Total']}</td>
                    <td class="text-center">${b['Death Rate Rural']}</td>
                    <td class="text-center">${b['Death Rate Urban']}</td>
                </tr>
            `);
            });

            if (indicatorData.density) {
                const density = indicatorData.density;

                const sorted = [...density].sort((a, b) => b['Population Density Total'] - a['Population Density Total']);
                $('#highestDensityState').text(sorted[0]['State/UT']);
                $('#highestDensityValue').text(sorted[0]['Population Density Total'] + ' /sq km');

                const lowestValid = sorted.filter(d => d['Population Density Total'] > 0);
                $('#lowestDensityState').text(lowestValid[lowestValid.length - 1]['State/UT']);
                $('#lowestDensityValue').text(lowestValid[lowestValid.length - 1]['Population Density Total'] + ' /sq km');

                const avgDensity = Math.round(density.reduce((sum, d) => sum + d['Population Density Total'], 0) / density.length);
                $('#avgDensity').text(avgDensity);

                const ctx = document.getElementById('densityChart');
                if (ctx) {
                    new Chart(ctx, {
                        type: 'bar',
                        data: {
                            labels: density.map(d => truncateLabel(d['State/UT'], 10)),
                            datasets: [
                                {
                                    label: 'Total Density',
                                    data: density.map(d => d['Population Density Total']),
                                    backgroundColor: 'rgba(13, 20, 253, 0.8)',
                                    borderRadius: 4
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
                                    backgroundColor: 'rgba(0, 67, 0, 0.8)',
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
                                        font: { size: 9, family: "'Inter', sans-serif", size: 11 },
                                        maxRotation: 45,
                                        minRotation: 45,
                                    }
                                },
                                y: {
                                    grid: { color: 'rgba(0, 76, 0, 0.05)' },
                                    ticks: {
                                        font: { family: "'Inter', sans-serif", size: 11 }
                                    }
                                }
                            }
                        }
                    });
                }

                const tbody = $('#densityTableBody');
                tbody.empty();
                density.forEach(d => {
                    tbody.append(`
                <tr>
                    <td>${d['State/UT']}</td>
                    <td class="text-center">${d['Population Density Total']}</td>
                    <td class="text-center">${d['Population Density Rural']}</td>
                    <td class="text-center">${d['Population Density Urban']}</td>
                </tr>
            `);
                });
            }
        }

        if (indicatorData.density) {
            const density = indicatorData.density;

            const sorted = [...density].sort((a, b) => b['Population Density Total'] - a['Population Density Total']);
            $('#highestDensityState').text(sorted[0]['State/UT']);
            $('#highestDensityValue').text(sorted[0]['Population Density Total'] + ' /sq km');

            const lowestValid = sorted.filter(d => d['Population Density Total'] > 0);
            $('#lowestDensityState').text(lowestValid[lowestValid.length - 1]['State/UT']);
            $('#lowestDensityValue').text(lowestValid[lowestValid.length - 1]['Population Density Total'] + ' /sq km');

            const avgDensity = Math.round(density.reduce((sum, d) => sum + d['Population Density Total'], 0) / density.length);
            $('#avgDensity').text(avgDensity);

            const ctx = document.getElementById('densityChart');
            if (ctx) {
                new Chart(ctx, {
                    type: 'bar',
                    data: {
                        labels: density.map(d => truncateLabel(d['State/UT'], 10)),
                        datasets: [
                            {
                                label: 'Total Density',
                                data: density.map(d => d['Population Density Total']),
                                backgroundColor: 'rgba(13, 110, 253, 0.8)',
                                borderRadius: 4
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
                                    font: { size: 9, family: "'Inter', sans-serif", size: 11 },
                                    maxRotation: 45,
                                    minRotation: 45,
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

            const tbody = $('#densityTableBody');
            tbody.empty();
            density.forEach(d => {
                tbody.append(`
                <tr>
                    <td>${d['State/UT']}</td>
                    <td class="text-center">${d['Population Density Total']}</td>
                    <td class="text-center">${d['Population Density Rural']}</td>
                    <td class="text-center">${d['Population Density Urban']}</td>
                </tr>
            `);
            });

        }
    }
}