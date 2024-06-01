import React from "react";


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
            <main className="flex-1 p-6 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                <card>
                    <div className="flex items-center justify-between card-header">
                        <h3>Total Users</h3>
                        <UsersIcon className="h-6 w-6 text-gray-500"/>
                    </div>
                    <div>
                        <div className="text-4xl font-bold">1,234</div>
                        <p className="text-gray-500 text-sm">+5.2% from last month</p>
                    </div>
                </card>
                <card>
                    <div className="flex items-center justify-between">
                        <div>Active Subscriptions</div>
                        <ShoppingCartIcon className="h-6 w-6 text-gray-500"/>
                    </div>
                    <div>
                        <div className="text-4xl font-bold">789</div>
                        <p className="text-gray-500 text-sm">+3.1% from last month</p>
                    </div>
                </card>
                <card>
                    <div className="flex items-center justify-between">
                        <div>Total Revenue</div>
                        <CreditcardIcon className="h-6 w-6 text-gray-500"/>
                    </div>
                    <div>
                        <div className="text-4xl font-bold">$45,231</div>
                        <p className="text-gray-500 text-sm">+8.4% from last month</p>
                    </div>
                </card>
                <card>
                    <div className="flex items-center justify-between">
                        <div>New Signups</div>
                        <ActivityIcon className="h-6 w-6 text-gray-500"/>
                    </div>
                    <div>
                        <div className="text-4xl font-bold">124</div>
                        <p className="text-gray-500 text-sm">+12.7% from last month</p>
                    </div>
                </card>
                <card>
                    <div className="flex items-center justify-between">
                        <div>Churn Rate</div>
                        <PercentIcon className="h-6 w-6 text-gray-500"/>
                    </div>
                    <div>
                        <div className="text-4xl font-bold">3.2%</div>
                        <p className="text-gray-500 text-sm">-0.5% from last month</p>
                    </div>
                </card>
                <card>
                    <div className="flex items-center justify-between">
                        <div>Lifetime Value</div>
                        <DollarSignIcon className="h-6 w-6 text-gray-500"/>
                    </div>
                    <div>
                        <div className="text-4xl font-bold">$1,234</div>
                        <p className="text-gray-500 text-sm">+4.2% from last month</p>
                    </div>
                </card>
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
