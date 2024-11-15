document.addEventListener('DOMContentLoaded', function () {
    // Fetch and render expenses chart
    fetch('/consumptionANDincome/weekly-expenses-by-category/')
        .then(response => response.json())
        .then(data => {
            const expenseCategories = data.expenses_by_category.map(entry => entry.category);
            const expenseTotals = data.expenses_by_category.map(entry => entry.total_amount);

            const expensesCtx = document.getElementById('expensesChart').getContext('2d');
            new Chart(expensesCtx, {
                type: 'pie',
                data: {
                    labels: expenseCategories,
                    datasets: [{
                        data: expenseTotals,
                        backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF', '#FF9F40'],
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            position: 'bottom',
                        },
                    },
                }
            });
        });

    // Fetch and render income chart
    fetch('/consumptionANDincome/weekly-income-by-category/')
        .then(response => response.json())
        .then(data => {
            const incomeCategories = data.income_by_category.map(entry => entry.category);
            const incomeTotals = data.income_by_category.map(entry => entry.total_amount);

            const incomeCtx = document.getElementById('incomeChart').getContext('2d');
            new Chart(incomeCtx, {
                type: 'pie',
                data: {
                    labels: incomeCategories,
                    datasets: [{
                        data: incomeTotals,
                        backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF', '#FF9F40'],
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            position: 'bottom',
                        },
                    },
                }
            });
        });
});

document.addEventListener('DOMContentLoaded', function () {
    const loadDataBtn = document.getElementById('loadDataBtn');
    const expensesChartCtx = document.getElementById('expensesCategoryChart').getContext('2d');
    const incomeChartCtx = document.getElementById('incomeCategoryChart').getContext('2d');

    let expensesChart, incomeChart;

    loadDataBtn.addEventListener('click', function () {
        const startDate = document.getElementById('startDate').value;
        const endDate = document.getElementById('endDate').value;

        if (!startDate || !endDate) {
            alert("Please select both start and end dates.");
            return;
        }

        loadExpensesData(startDate, endDate);
        loadIncomeData(startDate, endDate);
    });

    function loadExpensesData(startDate, endDate) {
        fetch(`/consumptionANDincome/expenses-by-category/?start_date=${startDate}&end_date=${endDate}`)
            .then(response => response.json())
            .then(data => {
                const categories = data.expenses_by_category.map(entry => entry.category);
                const totals = data.expenses_by_category.map(entry => entry.total_amount);

                if (expensesChart) expensesChart.destroy(); // Destroy previous chart instance if exists

                expensesChart = new Chart(expensesChartCtx, {
                    type: 'pie',
                    data: {
                        labels: categories,
                        datasets: [{
                            data: totals,
                            backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF', '#FF9F40'],
                        }]
                    },
                    options: {
                        responsive: true,
                        plugins: {
                            legend: {
                                position: 'bottom',
                            },
                        },
                    }
                });
            });
    }

    function loadIncomeData(startDate, endDate) {
        fetch(`/consumptionANDincome/income-by-category/?start_date=${startDate}&end_date=${endDate}`)
            .then(response => response.json())
            .then(data => {
                const categories = data.income_by_category.map(entry => entry.category);
                const totals = data.income_by_category.map(entry => entry.total_amount);

                if (incomeChart) incomeChart.destroy(); // Destroy previous chart instance if exists

                incomeChart = new Chart(incomeChartCtx, {
                    type: 'pie',
                    data: {
                        labels: categories,
                        datasets: [{
                            data: totals,
                            backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF', '#FF9F40'],
                        }]
                    },
                    options: {
                        responsive: true,
                        plugins: {
                            legend: {
                                position: 'bottom',
                            },
                        },
                    }
                });
            });
    }
});
