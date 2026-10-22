while true; do
    echo "******User Management******"
    echo "1. See all users"
    echo "2. Add user"
    echo "3. Check user details"
    echo "4. Set/Change passwd"
    echo "5. Delete user"
    echo "6. Check current user"
    echo "7. Exit"
    read -p "Enter any of above option: " option

    if [ -z "$option" ]; then
        echo "please select any option."
    fi

    case $option in
        1)
            echo "fetching all users..."
            sleep 1
            echo " "
            cut -d: -f1 /etc/passwd
            ;;
        2)
            read -p "Enter username to create: " user
            sudo useradd "$user"
            echo "user "$user" created."
            ;;
        3)
            read -p "Enter username to see details: " user
            id "$user"
            echo " " 
            ;;
        4)
            read -p "Enter username to set/change password: " user
            sudo passwd "$user"
            ;;
        5)
            read -p "Enter user to delete: " user
            sudo userdel "$user"
            echo "user deleted successfully."
            ;;
        6)
            user=$(who)
            echo "current logged-in user is "$user" "
            ;;
        7)
            echo "Exiting..."
            exit 0
            ;;
        *)
            echo "Invalid option! please choose from {1-6}"
            ;;
    esac
done

