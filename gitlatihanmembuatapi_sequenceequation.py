from flask import Flask, request
import base64

app= Flask(__name__)

#error handler

@app.errorhandler(401)
def unauthorized():
    return {'ERROR 401 - Unauthorized' : 'You are not authorized to access this resource'},401

@app.route('/sequence-equation', methods=['GET'])
def searchSequenceEquation():
    #authentification - basicauth
    username = 'guest'
    password = 'guest123'
    strauth = f'{username}:{password}'
    encryption = strauth.encode('ascii')
    base64_auth_str = f'Basic {str(base64.b64encode(encryption))[2:-1]}'
    header = request.headers.get('Authorization')
    # data validation error 401
    if header!= base64_auth_str:
       return unauthorized()
    
    #processing body parameter request
    data = request.json
    p=data['p']

    def permutationEquation(p):
        permutationpx=[]
        for x in range(1,len(p)+1):
            for y in range(len(p)) :
                if x == p[y] :
                    permutationpx.append(y+1)  
        permutationpy=[]
        for y in permutationpx:
            for i in range(len(p)):
                if y == p[i]:
                    permutationpy.append(i+1)
        return permutationpy
    
    result=permutationEquation(p)
    return {'result': result}

if __name__ == '__main__':
    app.run(debug=True, port=5005)