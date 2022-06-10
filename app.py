from application import factory

app = factory.create_app()

if __name__ == '__main__':
    app.debug = True
    app.run()
