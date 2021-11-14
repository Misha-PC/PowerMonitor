from app import app


if __name__ == '__main__':
    # post = ApiHistory(db.get_connection())
    # post.new('id-1', 1, 19.865)

    app.run(debug=True)
