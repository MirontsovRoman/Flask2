from flask import jsonify
from api import app, db, request
from api.models.author import AuthorModel
from api.models.quote import QuoteModel
from api.schemas.quote import quote_schema, quotes_schema


@app.route('/quotes', methods=["GET"])
def quotes():
    quotes = QuoteModel.query.all()
    # Возвращаем ВСЕ цитаты
    return quotes_schema.dump(quotes)


@app.get('/quotes/<int:quote_id>')
def quote_by_id(quote_id):
    quote = QuoteModel.query.get(quote_id)
    if quote is not None:
        return quote_schema.dump(quote), 200
    return {"Error": f"Quote with id={quote_id} not found"}, 404


@app.get('/authors/<int:author_id>/quotes')
def quotes_by_author_id(author_id):
    author = AuthorModel.query.get(author_id)
    if author is None:
        return {"Error": f"Author id={author_id} not found"}, 404
    quotes = author.quotes.all()
    # Возвращаем все цитаты автора
    return quotes_schema.dump(quotes), 200


@app.post('/authors/<int:author_id>/quotes')
def create_quote(author_id):
    quote_data = request.json
    author = AuthorModel.query.get(author_id)
    if author is None:
        return {"Error": f"Author id={author_id} not found"}, 404
    
    quote = QuoteModel(author, **quote_data)
    db.session.add(quote)
    db.session.commit()
    return jsonify(quote_schema.dump(quote)), 201


@app.put('/quotes/<int:quote_id>')
def edit_quote(quote_id):
    quote_data = request.json
    quote = QuoteModel.query.get(quote_id)
    if quote is None:
        return {"Error": f"Quote with id={quote_id} not found"}, 404
    for key, value in quote_data.items():
        setattr(quote, key, value)
    db.session.commit()
    return quote_schema.dump(quote), 200


@app.delete('/quotes/<int:quote_id>')
def delete_quote(quote_id):
    quote = QuoteModel.query.get(quote_id)
    if quote is None:
        return f"Quote with id={quote_id} not found", 404
    db.session.delete(quote)
    db.session.commit()
    return {"message": f"Quote with id={quote_id} has deleted"}, 200