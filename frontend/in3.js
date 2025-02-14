// Line Chart for Purchases
const ctx1 = document.getElementById('purchaseChart').getContext('2d');
const purchaseChart = new Chart(ctx1, {
    type: 'line',
    data: {
        labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        datasets: [{
            label: 'Purchases',
            data: [1200, 1500, 2212, 1800, 2300, 2100, 2500],
            borderColor: 'blue',
            borderWidth: 2,
            fill: false
        }]
    }
});

// Pie Chart for Sales Reports
const ctx2 = document.getElementById('salesChart').getContext('2d');
const salesChart = new Chart(ctx2, {
    type: 'doughnut',
    data: {
        labels: ['Chrome', 'IE', 'FireFox', 'Safari', 'Opera'],
        datasets: [{
            data: [13212, 10000, 9000, 8000, 7000],
            backgroundColor: ['red', 'blue', 'green', 'orange', 'purple']
        }]
    }
});

// Bar Chart for Stock Reports
const ctx3 = document.getElementById('stockChart').getContext('2d');
const stockChart = new Chart(ctx3, {
    type: 'bar',
    data: {
        labels: ['Firefox', 'Chrome', 'Opera', 'Safari', 'IE'],
        datasets: [{
            label: 'Stock Levels',
            data: [13212, 11000, 10000, 9000, 8000],
            backgroundColor: ['orange', 'blue', 'red', 'green', 'purple']
        }]
    }
});
