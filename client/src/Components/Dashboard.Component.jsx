import React from "react";

const Card = ({ children }) => (
  <div className="bg-white p-6 rounded-lg shadow-md max-h-[150px]">{children}</div>
);
const Dashboard = () => {
    return (
        <div className="flex-1 flex flex-col">
            <header className="bg-white border-b px-6 py-4 flex items-center justify-between">
                <div className="flex items-center gap-4">
                    <button variant="ghost" size="icon">
                        <MenuIcon className="h-6 w-6"/>
                    </button>
                    <input
                        type="search"
                        placeholder="Search..."
                        className="bg-gray-100 border-gray-200 rounded-md px-4 py-2 text-sm w-96"
                    />
                </div>
                <div className="flex items-center gap-4">
                    <button variant="ghost" size="icon">
                        <BellIcon className="h-6 w-6"/>
                        <span className="sr-only">Notifications</span>
                    </button>
                    {/*<DropdownMenu>
                        <DropdownMenuTrigger asChild>
                            <Avatar className="h-9 w-9">
                                <img src="/placeholder.svg" alt="@shadcn"/>
                                <AvatarFallback>JP</AvatarFallback>
                            </Avatar>
                        </DropdownMenuTrigger>
                        <DropdownMenuContent>
                            <DropdownMenuItem>My Account</DropdownMenuItem>
                            <DropdownMenuItem>Settings</DropdownMenuItem>
                            <DropdownMenuSeparator/>
                            <DropdownMenuItem>Logout</DropdownMenuItem>
                        </DropdownMenuContent>
                    </DropdownMenu>*/}
                </div>
            </header>
            <main className="flex-1 ">
                <div className='flex-1 p-6 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4'>
                   <Card>
                    <div className="flex items-center justify-between Card-header">
                        <h3 className="text-lg font-semibold text-gray-800">Total Users</h3>
                        <UsersIcon className="h-6 w-6 text-gray-500"/>
                    </div>
                    <div className='items-center content-center h-full w-full'>
                        <div className="text-4xl font-bold">1,234</div>
                        <p className="text-gray-500 text-sm">+5.2% from last month</p>
                    </div>
                </Card>
                <Card>
                    <div className="flex items-center justify-between">
                        <div>Active Subscriptions</div>
                        <ShoppingCartIcon className="h-6 w-6 text-gray-500"/>
                    </div>
                    <div>
                        <div className="text-4xl font-bold">789</div>
                        <p className="text-gray-500 text-sm">+3.1% from last month</p>
                    </div>
                </Card>
                <Card>
                    <div className="flex items-center justify-between">
                        <div>Total Revenue</div>
                        <CreditCardIcon className="h-6 w-6 text-gray-500"/>
                    </div>
                    <div>
                        <div className="text-4xl font-bold">$45,231</div>
                        <p className="text-gray-500 text-sm">+8.4% from last month</p>
                    </div>
                </Card>
                <Card>
                    <div className="flex items-center justify-between">
                        <div>New Signups</div>
                        <ActivityIcon className="h-6 w-6 text-gray-500"/>
                    </div>
                    <div>
                        <div className="text-4xl font-bold">124</div>
                        <p className="text-gray-500 text-sm">+12.7% from last month</p>
                    </div>
                </Card>
                <Card>
                    <div className="flex items-center justify-between">
                        <div>Churn Rate</div>
                        <PercentIcon className="h-6 w-6 text-gray-500"/>
                    </div>
                    <div>
                        <div className="text-4xl font-bold">3.2%</div>
                        <p className="text-gray-500 text-sm">-0.5% from last month</p>
                    </div>
                </Card>
                <Card>
                    <div className="flex items-center justify-between">
                        <div>Lifetime Value</div>
                        <DollarSignIcon className="h-6 w-6 text-gray-500"/>
                    </div>
                    <div>
                        <div className="text-4xl font-bold">$1,234</div>
                        <p className="text-gray-500 text-sm">+4.2% from last month</p>
                    </div>
                </Card>
                </div>

            </main>
        </div>
)
}

function MenuIcon(props) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <line x1="4" x2="20" y1="12" y2="12" />
      <line x1="4" x2="20" y1="6" y2="6" />
      <line x1="4" x2="20" y1="18" y2="18" />
    </svg>
  )
}

function ActivityIcon(props) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="M22 12h-2.48a2 2 0 0 0-1.93 1.46l-2.35 8.36a.25.25 0 0 1-.48 0L9.24 2.18a.25.25 0 0 0-.48 0l-2.35 8.36A2 2 0 0 1 4.49 12H2" />
    </svg>
  )
}


function BellIcon(props) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9" />
      <path d="M10.3 21a1.94 1.94 0 0 0 3.4 0" />
    </svg>
  )
}


function CreditCardIcon(props) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <rect width="20" height="14" x="2" y="5" rx="2" />
      <line x1="2" x2="22" y1="10" y2="10" />
    </svg>
  )
}


function DollarSignIcon(props) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <line x1="12" x2="12" y1="2" y2="22" />
      <path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6" />
    </svg>
  )
}





function MountainIcon(props) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="m8 3 4 8 5-5 5 15H2L8 3z" />
    </svg>
  )
}


function SettingsIcon(props) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0-.73 2.73l.22.38a2 2 0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 0l.15.08a2 2 0 0 0 2.73-.73l.22-.39a2 2 0 0 0-.73-2.73l-.15-.08a2 2 0 0 1-1-1.74v-.5a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 0 0-2-2z" />
      <circle cx="12" cy="12" r="3" />
    </svg>
  )
}


const PercentIcon = () => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    className="h-6 w-6"
    fill="none"
    viewBox="0 0 24 24"
    stroke="currentColor"
  >
    <path
      strokeLinecap="round"
      strokeLinejoin="round"
      strokeWidth="2"
      d="M3 11a9 9 0 0118 0M5 14a7 7 0 0014 0M10 19l4-4m0 0l-4-4m4 4H6"
    />
  </svg>
);


function ShoppingCartIcon(props) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <circle cx="8" cy="21" r="1" />
      <circle cx="19" cy="21" r="1" />
      <path d="M2.05 2.05h2l2.66 12.42a2 2 0 0 0 2 1.58h9.78a2 2 0 0 0 1.95-1.57l1.65-7.43H5.12" />
    </svg>
  )
}


function UsersIcon(props) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2" />
      <circle cx="9" cy="7" r="4" />
      <path d="M22 21v-2a4 4 0 0 0-3-3.87" />
      <path d="M16 3.13a4 4 0 0 1 0 7.75" />
    </svg>
  )
}


export {Dashboard}