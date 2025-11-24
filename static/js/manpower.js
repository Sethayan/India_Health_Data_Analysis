function initializeManPowerStats(manpowerData) {

    if (manpowerData.doctors) {

        const doctors = manpowerData.doctors;
        let totalRequired = 0, totalPosition = 0, totalSanctioned = 0, totalVacant = 0;

        doctors.forEach(d => {
            totalRequired += d['Required 2023'] || 0;
            totalPosition += d['In Position 2023'] || 0;
            totalSanctioned += d['Sanctioned 2023'] || 0;
            totalVacant += d['Vacant 2023'] || 0;
        });

        $('#doctorsRequired').text(totalRequired);
        $('#doctorsPosition').text(totalPosition);
        $('#doctorsSanctioned').text(totalSanctioned);
        $('#doctorsVacant').text(totalVacant);

        const ctx = document.getElementById('doctorsStateChart');
        if (ctx) {
            new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: doctors.slice(0, 20).map(d => truncateLabel(d['State/UT'], 10)),
                    datasets: [{
                        label: 'In Position 2023',
                        data: doctors.slice(0, 20).map(d => d['In Position 2023']),
                        backgroundColor: 'rgba(25,135,84,0.8)',
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
                                font: { family: "'Inter', sans-serif", size: 12 }
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
                        x: { grid: { display: false }, ticks: { font: { size: 11 } } },
                        y: { grid: { color: 'rgba(0,0,0,0.05)' }, ticks: { font: { size: 11 } } }
                    }
                }
            });
        }

        const compCtx = document.getElementById('doctorsCompChart');
        if (compCtx) {
            new Chart(compCtx, {
                type: 'bar',
                data: {
                    labels: doctors.slice(0, 15).map(d => truncateLabel(d['State/UT'], 8)),
                    datasets: [
                        {
                            label: '2005',
                            data: doctors.slice(0, 15).map(d => d['In Position 2005'] || 0),
                            backgroundColor: 'rgba(13, 110, 253, 0.2)',
                            borderColor: 'rgba(13, 110, 253, 0.8)',
                            borderWidth: 1
                        },
                        {
                            label: '2023',
                            data: doctors.slice(0, 15).map(d => d['In Position 2023'] || 0),
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
                                font: { family: "'Inter', sans-serif", size: 12 }
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
                        x: { ticks: { maxRotation: 45, minRotation: 45 } },
                        y: { grid: { color: 'rgba(0,0,0,0.05)' } }
                    }
                }
            });
        }


        if (manpowerData.specialists) {

            const specs = manpowerData.specialists;
            let totalRequired = 0, totalPosition = 0, totalShortfall = 0;

            specs.forEach(s => {
                totalRequired += s['Required 2023'] || 0;
                totalPosition += s['In Position 2023'] || 0;
                totalShortfall += s['Shortfall 2023'] || 0;
            });

            $('#specialistsRequired').text(totalRequired);
            $('#specialistsPosition').text(totalPosition);
            $('#specialistsShortfall').text(totalShortfall);

            const ctxSpecs = document.getElementById('specialistsChart');
            if (ctxSpecs) {
                new Chart(ctxSpecs, {
                    type: 'bar',
                    data: {
                        labels: specs.map(s => truncateLabel(s['State/UT'], 10)),
                        datasets: [
                            {
                                label: 'Required',
                                data: specs.map(s => s['Required 2023']),
                                backgroundColor: 'rgba(13, 110, 253, 0.2)',
                                borderColor: 'rgba(13, 110, 253, 0.8)',
                                borderWidth: 1
                            },
                            {
                                label: 'In Position',
                                data: specs.map(s => s['In Position 2023']),
                                backgroundColor: 'rgba(25, 135, 84, 0.2)',
                                borderColor: 'rgba(25, 135, 84, 0.8)',
                                borderWidth: 1
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
                                    font: { family: "'Inter', sans-serif", size: 12 }
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
                            x: { ticks: { font: { size: 11 } }, grid: { display: false } },
                            y: { grid: { color: 'rgba(0,0,0,0.05)' } }
                        }
                    }
                });
            }

            const specBody = $('#specialistsTableBody');
            specBody.empty();
            specs.forEach(s => {
                specBody.append(`
                <tr>
                    <td>${s['State/UT']}</td>
                    <td class="text-center">${(s['Required 2023'] || 0)}</td>
                    <td class="text-center">${(s['Sanctioned 2023'] || 0)}</td>
                    <td class="text-center">${(s['In Position 2023'] || 0)}</td>
                    <td class="text-center text-danger">${(s['Vacant 2023'] || 0)}</td>
                    <td class="text-center text-warning">${(s['Shortfall 2023'] || 0)}</td>
                </tr>
            `);
            });
        }

        const docBody = $('#doctorsTableBody');
        docBody.empty();
        doctors.forEach(d => {
            docBody.append(`
                <tr>
                    <td>${d['State/UT']}</td>
                    <td class="text-center">${(d['Required 2023'] || 0)}</td>
                    <td class="text-center">${(d['Sanctioned 2023'] || 0)}</td>
                    <td class="text-center">${(d['In Position 2023'] || 0)}</td>
                    <td class="text-center text-danger">${(d['Vacant 2023'] || 0)}</td>
                    <td class="text-center text-warning">${(d['Shortfall 2023'] || 0)}</td>
                </tr>
            `);
        });

           if (manpowerData.nursing) {

        const nursing = manpowerData.nursing;
        let totalRequired = 0, totalPosition = 0, totalVacant = 0;

        nursing.forEach(n => {
            totalRequired += n['Required 2023'] || 0;
            totalPosition += n['In Position 2023'] || 0;
            totalVacant += n['Vacant 2023'] || 0;
        });

        $('#nursingRequired').text(totalRequired);
        $('#nursingPosition').text(totalPosition);
        $('#nursingVacant').text(totalVacant);

        const ctxNursing = document.getElementById('nursingChart');
        if (ctxNursing) {
            new Chart(ctxNursing, {
                type: 'bar',
                data: {
                    labels: nursing.map(n => truncateLabel(n['State/UT'], 10)),
                    datasets: [{
                        label: 'In Position 2023',
                        data: nursing.map(n => n['In Position 2023']),
                        backgroundColor:'rgba(13, 202, 240, 0.8)' ,
                        borderRadius: 4
                    }]
                },
                options: {
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            position: 'top',
                            labels: {
                                usePointStyle: true,
                                padding: 15,
                                font: { family: "'Inter', sans-serif", size: 12 }
                            }
                        },
                        tooltip: {
                            backgroundColor: 'rgba(0,0,0,0.8)',
                            titleFont: { family: "'Inter', sans-serif", size: 13 },
                            bodyFont: { family: "'Inter', sans-serif", size: 12 },
                            padding: 12,
                            cornerRadius: 8
                        }
                    },
                    scales: {
                        x: { ticks: { font: { size: 11 }}, grid: { display: false }},
                        y: { grid: { color: 'rgba(0,0,0,0.05)' } }
                    }
                }
            });
        }

        const nursingBody = $('#nursingTableBody');
        nursingBody.empty();
        nursing.forEach(n => {
            nursingBody.append(`
                <tr>
                    <td>${n['State/UT']}</td>
                    <td class="text-center">${(n['Required 2023'] || 0)}</td>
                    <td class="text-center">${(n['Sanctioned 2023'] || 0)}</td>
                    <td class="text-center">${(n['In Position 2023'] || 0)}</td>
                    <td class="text-center text-danger">${(n['Vacant 2023'] || 0)}</td>
                    <td class="text-center text-warning">${(n['Shortfall 2023'] || 0)}</td>
                </tr>
            `);
        });
    }
    }
}

