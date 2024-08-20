import {ActivityIcon, BellIcon, MountainIcon, OrdersIcon, SettingsIcon, StockIcon, UsersIcon} from "../Assets/Svg";

const SideBar = [
    {
        name: "Dashboard",
        href:'/',
        icon: MountainIcon
    },{
        name: "Waste Tracking",
        href: "?Waste",
        icon: ActivityIcon,
    },
    {
        name: "Inventory",
        icon: BellIcon,
        children: [
            {
                name: 'Inventory Forecasting',
                href: '/Forecasting'
            },
            {
                name: 'Inventory History',
                href: '/Inventory History'
            }
        ]
    },
    {
        name: "Administration",
        href: "#",
        icon: UsersIcon,
        children: [
            {
                name: 'Users Management',
                href: '/Users'
            },
            {
                name: 'Category Management',
                href: '/Category'
            },
            {
                name:'Supplier Management',
                href: '/Supplier'
            },
            {
                name: 'Product Management',
                href: '/Product'
            },
            {
                name: 'Unit Management',
                href: '/Unit'
            },
            {
                name: 'Client Management',
                href: '/Client'
            },
            {
                name: 'Service Management',
                href: '/Service'
            }
        ]
    },
    {
        name: "Orders",
        href: '/Orders',
        icon: OrdersIcon
    },
    {
        name: "Stock",
        icon: StockIcon,
        children: [
            {
                name: 'Stock Analytics',
                href: '/Analytics'
            },
            {
                name: 'Stock Reports',
                href: '/Stock Reports'
            },
            {
                name:'Stock Movement',
                href: '/Stock Movement'
            },
            {
                name: 'Stock Alerts',
                href: '/Stock Alerts'
            }
        ]
    },
    {
        name: "Settings",
        href: "#",
        icon: SettingsIcon,
        children: [
            {
                name: 'Profile Settings',
                href: '/Profile'
            },
            {
                name: 'Change Password',
                href: '/Change Password'
            }
        ]
    },
];

export {SideBar}