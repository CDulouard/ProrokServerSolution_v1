using System;

namespace Exemple
{
    public class Employe : Perso
    {
        private string _job;
        public Employe(string nom, int age, string job) : base(nom, age)
        {
            this._job = job;
        }

        public new void SePresenter()
        {
            Console.WriteLine("Bonjour je m'appel " + _name + " et j'ai " + _age.ToString() + " ans et je suis un " +
                              espece + ".\n Mon metier est " + _job + ".");
        }

        public void ChangerDeMetier(string metier)
        {
            this._job = metier;
        }
        
    }
}