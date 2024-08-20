import React, { useEffect, useRef } from "react";
import { UsersIcon, ActivityIcon, CreditCardIcon, DollarSignIcon, ShoppingCartIcon, PercentIcon } from '../Assets/Svg';
import { Chart, registerables } from 'chart.js';

Chart.register(...registerables);

const Card = ({ children }) => (
  <div className="bg-white p-6 rounded-lg shadow-md max-h-[150px]">{children}</div>
);

const Dashboard = () => {
  const barChartRef = useRef(null);
  const pieChartRef = useRef(null);

  useEffect(() => {
    let barChartInstance;
    let pieChartInstance;

    if (barChartRef.current) {
      barChartInstance = new Chart(barChartRef.current, {
        type: 'bar',
        data: {
          labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
          datasets: [
            {
              label: 'Sales',
              data: [12, 19, 3, 5, 2, 3],
              backgroundColor: 'rgba(75, 192, 192, 0.2)',
              borderColor: 'rgba(75, 192, 192, 1)',
              borderWidth: 1,
            },
          ],
        },
        options: {
          scales: {
            y: {
              beginAtZero: true,
            },
          },
        },
      });
    }

    if (pieChartRef.current) {
      pieChartInstance = new Chart(pieChartRef.current, {
        type: 'doughnut',
        data: {
          labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
          datasets: [
            {
              label: '# of Votes',
              data: [12, 19, 3, 5, 2, 3],
              backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)',
              ],
              borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
              ],
              borderWidth: 1,
            },
          ],
        },
      });
    }

    return () => {
      if (barChartInstance) {
        barChartInstance.destroy();
      }
      if (pieChartInstance) {
        pieChartInstance.destroy();
      }
    };
  }, []);

  return (
    <div className="flex-1 flex flex-col">
      <main className="flex-1">
        <div className='flex-1 p-6 grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-4'>
          <Card>
            <div className="flex items-center justify-between">
              <h3 className="text-lg font-semibold text-gray-800">Current Stock</h3>
              <UsersIcon className="h-6 w-6 text-gray-500" />
            </div>
            <div className='h-full w-full'>
              <div className="text-4xl font-bold">1,234</div>
              <p className="text-gray-500 text-sm"><span className="text-green-600 font-semibold">+5.2% </span>from last month</p>
            </div>
          </Card>
          <Card>
            <div className="flex items-center justify-between">
              <h3 className="text-lg font-semibold text-gray-800">Outbound Stock</h3>
              <ShoppingCartIcon className="h-6 w-6 text-gray-500" />
            </div>
            <div>
              <div className="text-4xl font-bold">789</div>
              <p className="text-gray-500 text-sm"><span className="text-green-600 font-semibold">+3.1% </span>from last month</p>
            </div>
          </Card>
          <Card>
            <div className="flex items-center justify-between">
              <h3 className="text-lg font-semibold text-gray-800">Total Revenue</h3>
              <CreditCardIcon className="h-6 w-6 text-gray-500" />
            </div>
            <div>
              <div className="text-4xl font-bold">$45,231</div>
              <p className="text-gray-500 text-sm"><span className="text-green-600 font-semibold">+8.4%</span> from last month</p>
            </div>
          </Card>
          <Card>
            <div className="flex items-center justify-between">
              <h3 className="text-lg font-semibold text-gray-800">Inbound Stock</h3>
              <ActivityIcon className="h-6 w-6 text-gray-500" />
            </div>
            <div>
              <div className="text-4xl font-bold">124</div>
              <p className="text-gray-500 text-sm"><span className="text-green-600 font-semibold">+12.7%</span> from last month</p>
            </div>
          </Card>
        </div>
        <div className="p-6 grid grid-cols-1 md:grid-cols-2 gap-4">
          <div className="bg-white p-6 rounded-lg shadow-md shadow-md min-w-[650px] min-h-[550px]">
            <h3 className="text-lg font-semibold text-gray-800 mb-4">Sales Over Time</h3>
            <canvas ref={barChartRef}></canvas>
          </div>
          <div className="bg-white p-6 rounded-lg shadow-md min-w-[550px] h-[600px]">
            <h3 className="text-lg font-semibold text-gray-800 mb-4">Sales Distribution</h3>
            <canvas ref={pieChartRef} className='max-h-[500px]'></canvas>
          </div>
        </div>
      </main>
    </div>
  );
}

export default Dashboard;
