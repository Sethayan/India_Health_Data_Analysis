function initComparisonCharts(comparisonData, yearlyData) {
    if (comparisonData && comparisonData.infra_comparison) {
        const infra = comparisonData.infra_comparison;
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


    }
} 