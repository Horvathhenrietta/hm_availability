from win10toast import ToastNotifier

toast = ToastNotifier()


def notify_available(article, size):
    title = 'Articles available'
    body = f"Article ({article}) is available in size {size} :)."
    toast.show_toast(
        title,
        body,
        icon_path=None,
        duration=20,
        threaded=True,
    )
    return 0


if __name__ == "__main__":
    notify_available("1044156002", "38")
