# Q-learning-agent-for-maze-escaping

Modificari aduse fata de proiectul initial:

* am reparat bug-ul care cauza obtinerea mai multor drumuri optime(daca aveam drumuri de lungimi egale nu alegeam drumul de recompensa maxima, de aceea puteau sa apara mai multe drumuri optime pentru un robot)
* am schimbat strategia pentru asignarea scorului, acum calculez mai bine, ca suma a tuturor recompenselor date de perechile de forma (stare, actiune) prin care trec (inainte scorul returnat era doar valoarea din tabela Q corespunzatorare starii si actiunii care ma duce la finish): aceasta schimbare determina o dependenta mai mica fata de starea finala
* criteriul de optimalitate a drumului e dat de un raport de tip Greedy:  <sup>total_reward</sup>/<sub>path_length</sub>
* implementarea unei interfete grafice simple care permite utilizatorului sa vizualizeze in timp real evolutia traseului unui robot la alegere
* adaugarea unor pedepse de tipul "stai n ture"
* oferirea posibilitatii revenirii la stari anterioare cel mult o singura data pe episod
