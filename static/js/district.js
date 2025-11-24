function ViewDistrictData(allDistricts) {
    let currentPage = 1;
    const itemsPerPage = 20;
    let filteredData = [...allDistricts];
    let sortField = null;
    let sortDirection = 'asc';

    function updateSummary() {
        $('#totalDistricts').text(filteredData.length);
        $('#totalPHCs').text(filteredData.reduce((sum, d) => sum + d.phc_rural + d.phc_urban, 0).toLocaleString());
        $('#totalCHCs').text(filteredData.reduce((sum, d) => sum + d.chc_rural + d.chc_urban, 0).toLocaleString());
        $('#totalMC').text(filteredData.reduce((sum, d) => sum + d.mc, 0));
    }

    function renderTable() {
        const start = (currentPage - 1) * itemsPerPage;
        const end = start + itemsPerPage;
        const pageData = filteredData.slice(start, end); // for pagination this is used. 

        const tbody = $('#districtTableBody');
        tbody.empty();

        pageData.forEach(d => {
            tbody.append(`
                <tr>
                    <td>${d.state}</td>
                    <td>${d.district}</td>
                    <td class="text-center">${d.sc_rural}</td>
                    <td class="text-center">${d.sc_urban}</td>
                    <td class="text-center">${d.phc_rural}</td>
                    <td class="text-center">${d.phc_urban}</td>
                    <td class="text-center">${d.chc_rural}</td>
                    <td class="text-center">${d.chc_urban}</td>
                    <td class="text-center">${d.sdh}</td>
                    <td class="text-center">${d.dh}</td>
                    <td class="text-center">${d.mc}</td>
                </tr>
            `);
        });

        renderPagination();
    }

    function renderPagination() {
        const totalPages = Math.ceil(filteredData.length / itemsPerPage);
        const pagination = $('#pagination');
        pagination.empty();

        if (totalPages <= 1) return;

        pagination.append(`
            <li class="page-item ${currentPage === 1 ? 'disabled' : ''}">
                <a class="page-link" href="#" data-page="${currentPage - 1}">Previous</a>
            </li>
        `);

        const startPage = Math.max(1, currentPage - 2);
        const endPage = Math.min(totalPages, currentPage + 2);

        if (startPage > 1) {
            pagination.append(`<li class="page-item"><a class="page-link" href="#" data-page="1">1</a></li>`);
            if (startPage > 2) {
                pagination.append(`<li class="page-item disabled"><span class="page-link">...</span></li>`);
            }
        }

        for (let i = startPage; i <= endPage; i++) {
            pagination.append(`
                <li class="page-item ${i === currentPage ? 'active' : ''}">
                    <a class="page-link" href="#" data-page="${i}">${i}</a>
                </li>
            `);
        }

        if (endPage < totalPages) {
            if (endPage < totalPages - 1) {
                pagination.append(`<li class="page-item disabled"><span class="page-link">...</span></li>`);
            }
            pagination.append(`<li class="page-item"><a class="page-link" href="#" data-page="${totalPages}">${totalPages}</a></li>`);
        }

        pagination.append(`
            <li class="page-item ${currentPage === totalPages ? 'disabled' : ''}">
                <a class="page-link" href="#" data-page="${currentPage + 1}">Next</a>
            </li>
        `);
    }

    function filterData() {
        const state = $('#stateSelect').val();
        const search = $('#districtSearch').val().toLowerCase();

        filteredData = allDistricts.filter(d => {
            const stateMatch = !state || d.state === state;
            const searchMatch = !search || d.district.toLowerCase().includes(search) || d.state.toLowerCase().includes(search);
            return stateMatch && searchMatch;
        });

        currentPage = 1;
        updateSummary();
        renderTable();
        updateStateChart();
    }

    function updateStateChart() {
        const stateData = {};
        filteredData.forEach(d => {
            if (!stateData[d.state]) {
                stateData[d.state] = { phc: 0, chc: 0, dh: 0 };
            }
            stateData[d.state].phc += d.phc_rural + d.phc_urban;
            stateData[d.state].chc += d.chc_rural + d.chc_urban;
            stateData[d.state].dh += d.dh;
        });

        const labels = Object.keys(stateData).slice(0, 15);
        const phcData = labels.map(s => stateData[s].phc);
        const chcData = labels.map(s => stateData[s].chc);

        const ctx = document.getElementById('stateDistrictChart');
        if (ctx) {
            const existingChart = Chart.getChart(ctx);
            if (existingChart) existingChart.destroy();

            new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: labels.map(l => truncateLabel(l, 12)),
                    datasets: [
                        {
                            label: 'Total PHCs',
                            data: phcData,
                            backgroundColor: 'rgba(25, 135, 84, 0.8)',
                            borderRadius: 4
                        },
                        {
                            label: 'Total CHCs',
                            data: chcData,
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
                                maxRotation: 45, minRotation: 45,
                                font: { family: "'Inter', sans-serif", size: 11 }
                            },
                        },
                        y: {
                            grid: { color: 'rgba(0, 0, 0, 0.05)' },
                            ticks: {
                                font: { family: "'Inter', sans-serif", size: 11 }
                            },
                            beginAtZero: true
                        }


                    }
                }
            });
        }
    }

    $('#applyFilter').on('click', filterData);
    $('#resetFilter').on('click', function () {
        $('#stateSelect').val('');
        $('#districtSearch').val('');
        filterData();
    });

    $('#districtSearch').on('keyup', function (e) {
        if (e.key === 'Enter') filterData();
    });

    $(document).on('click', '#pagination .page-link', function (e) {
        e.preventDefault();
        const page = $(this).data('page');
        if (page && page >= 1 && page <= Math.ceil(filteredData.length / itemsPerPage)) {
            currentPage = page;
            renderTable();
        }
    });

    updateSummary();
    renderTable();
    updateStateChart();
}
