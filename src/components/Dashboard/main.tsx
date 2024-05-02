import React, { useEffect } from 'react';
import Chart from 'chart.js';

const DashboardHome: React.FC = () => {
  useEffect(() => {
    const buyersChart = new Chart(document.getElementById('buyers-chart') as HTMLCanvasElement, buyersData);
    const reviewsChart = new Chart(document.getElementById('reviews-chart') as HTMLCanvasElement, reviewsData);

    return () => {
      buyersChart.destroy();
      reviewsChart.destroy();
    };
  }, []);

  const buyersData = {
    type: 'line',
    data: {
      labels: ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
      datasets: [{
        backgroundColor: "rgba(99,179,237,0.4)",
        borderColor: "#63b3ed",
        pointBackgroundColor: "#fff",
        pointBorderColor: "#63b3ed",
        data: [203,156,99,251,305,247,256]
      },
      {
        backgroundColor: "rgba(198,198,198,0.4)",
        borderColor: "#f7fafc",
        pointBackgroundColor: "#fff",
        pointBorderColor: "#f7fafc",
        data: [86,97,144,114,94,108,156]
      }]
    },
    options: {
      legend: {
        display: false
      },
      scales: {
        yAxes: [{
          gridLines: {
            display:false
          },
          ticks: {
            display: false
          }
        }],
        xAxes: [{
          gridLines: {
            display: false
          }
        }]
      }
    }
  };

  const reviewsData = {
    type: 'bar',
    data: {
      labels: ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
      datasets: [{
        backgroundColor: "rgba(99,179,237,0.4)",
        borderColor: "#63b3ed",
        pointBackgroundColor: "#fff",
        pointBorderColor: "#63b3ed",
        data: [203,156,99,251,305,247,256]
      }]
    },
    options: {
      legend: {
        display: false
      },
      scales: {
        yAxes: [{
          gridLines: {
            display:false
          },
          ticks: {
            display: false
          }
        }],
        xAxes: [{
          gridLines: {
            display: false
          }
        }]
      }
    }
  };

  return (
    <div id="home">
      {/* breadcrumb */}
      <nav className="text-sm font-semibold mb-6" aria-label="Breadcrumb">
        <ol className="list-none p-0 inline-flex">
          <li className="flex items-center text-blue-500">
            <a href="#" className="text-gray-700">Home</a>
            <svg className="fill-current w-3 h-3 mx-3" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 512"><path d="M285.476 272.971L91.132 467.314c-9.373 9.373-24.569 9.373-33.941 0l-22.667-22.667c-9.357-9.357-9.375-24.522-.04-33.901L188.505 256 34.484 101.255c-9.335-9.379-9.317-24.544.04-33.901l22.667-22.667c9.373-9.373 24.569-9.373 33.941 0L285.475 239.03c9.373 9.372 9.373 24.568.001 33.941z"/></svg>
          </li>
          <li className="flex items-center">
            <a href="#" className="text-gray-600">Dashboard</a>
          </li>
        </ol>
      </nav>
      {/* breadcrumb end */}

      <div className="lg:flex justify-between items-center mb-6">
        <p className="text-2xl font-semibold mb-2 lg:mb-0">Good afternoon, Joe!</p>
        <button className="bg-blue-500 hover:bg-blue-600 focus:outline-none rounded-lg px-6 py-2 text-white font-semibold shadow">View Logs</button>
      </div>

      <div className="flex flex-wrap -mx-3 mb-20">
        {/* Card components */}
      </div>

      <div className="flex flex-wrap -mx-3">
        {/* Chart components */}
      </div>
    </div>
  );
};

export default DashboardHome;