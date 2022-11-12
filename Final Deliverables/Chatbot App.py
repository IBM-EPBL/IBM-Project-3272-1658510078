from flask import Flask,render_template
app=Flask(_name_)
@app.route('/')
def bank():
    return render_template('BankingChatbot.html')
if _name_ =='_main_':
    app.run()
