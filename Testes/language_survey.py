from survey import AnonymousSurvey

question = "What language did u first learn to speek"
my_survey = AnonymousSurvey(question)

#Mostra a pergunta e armazena as respostas da pergunta
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

#Exibe os resultados da pesquisa
print("\n Thank u to everyone who participated in the survey!")
my_survey.show_results()