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
