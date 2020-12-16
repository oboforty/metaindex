from webapp.website import MetaIndexWebsite

# this can be used for Gunicorn as well
app = MetaIndexWebsite()


if __name__ == "__main__":
    # run it manually:
    app.start()
