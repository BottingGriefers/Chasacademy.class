import time


for j in range(3):
    print(j)
#Range function ger oss ett intervalv, 
for index in range(5, 0, -1): 
    print(index)
    time.sleep(1)



    #git add gör att det lägger upp filerna i din stash eller till commit, när du har lagt upp alla filer du vill ladda upp på #
    # github måste du efteråt "git commit" den då den kommer säga till dig skriv en kommentar och kolla om du vill skicka demdär filerna som du git adda
    #sen när du har skickat alla filer till commit måste du göra ett sista steg som är "Git push" Det drar alla filer till ditt gihub inuti din repository.
    # Man vill göra branches som är som en isolation från main branch det gör man för att skydda den viktiga koden och testa den på en branch som är mindre värd
    # du ska nämna dina branches för det dem är, t.ex(mobil app) nämn det mobil att, (python script), nämn branchen python script
    # Pull request gör att man tar ner koden från github reposotory och då kollar den nya saker som blir ändrade och dina nuvarande saker cle