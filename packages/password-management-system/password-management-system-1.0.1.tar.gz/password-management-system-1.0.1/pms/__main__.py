import argparse
from pms import user_controller
from pms import password_controller
from pms import utility_functions


def main():
    global_parser = argparse.ArgumentParser()
    subparsers = global_parser.add_subparsers(
        dest="subparser_name",
        title="subcommands",
        help="password management system"
    )

    generate_password_parser = subparsers.add_parser("generate", help="generate a password")
    generate_password_parser.add_argument("-l", "--long", action="store", type=int, default=16)
    generate_password_parser.add_argument("-q", "--query", nargs="+")

    evaluate_password_parser = subparsers.add_parser("evaluate", help="evaluate the strength of a password")
    evaluate_password_parser.add_argument("password")

    signup_parser = subparsers.add_parser("signup", help="signup user")
    signup_parser.add_argument("username")
    signup_parser.add_argument("password")

    login_parser = subparsers.add_parser("login", help="login")
    login_parser.add_argument("username")
    login_parser.add_argument("password")

    logout_parser = subparsers.add_parser("logout", help="logout")

    show_user_parser = subparsers.add_parser("user", help="show logged user if found")

    add_password_parser = subparsers.add_parser("add", help="add password")
    add_password_parser.add_argument("new_password")
    add_password_parser.add_argument("name")
    add_password_parser.add_argument("-w", "--website", action="store")
    add_password_parser.add_argument("-d", "--description", action="store")

    show_password_parser = subparsers.add_parser("show", help="show passwords")
    show_password_parser.add_argument("-n", "--name", action="store", default=None)
    show_password_parser.add_argument("-w", "--website", action="store", default=None)
    show_password_parser.add_argument("-i", "--id", action="store", default=None)

    delete_password_parser = subparsers.add_parser("delete", help="delete password")
    delete_password_parser.add_argument("id")

    delete_user_parser = subparsers.add_parser("delete_user", help="delete user")
    delete_user_parser.add_argument("username")
    delete_user_parser.add_argument("password")

    update_password_parser = subparsers.add_parser("update", help="update password")
    update_password_parser.add_argument("id")
    update_password_parser.add_argument("-p", "--password", default=None)
    update_password_parser.add_argument("-n", "--name", default=None)
    update_password_parser.add_argument("-w", "--website", default=None)
    update_password_parser.add_argument("-d", "--description", default=None)

    args = global_parser.parse_args()

    subcommand = args.subparser_name
    match subcommand:
        case "generate":
            utility_functions.generate_password(args.long, args.query)
        case "evaluate":
            utility_functions.evaluate_password(args.password)
        case "signup":
            user_controller.signup_user(args.username, args.password)
        case "add":
            password_controller.add_password(args.new_password,
                                             args.name,
                                             args.website,
                                             args.description)
        case "show":
            password_controller.select_password(args.name,
                                                args.website,
                                                args.id)
        case "delete":
            password_controller.delete_password(args.id)
        case "login":
            user_controller.login_user(args.username, args.password)
        case "logout":
            user_controller.logout()
        case "user":
            user_controller.display_logged_user()
        case "delete_user":
            user_controller.delete_user(args.username, args.password)
        case "update":
            password_controller.update_password(args.id, args.password, args.name, args.website, args.description)


if __name__ =="__main__":
    main()
