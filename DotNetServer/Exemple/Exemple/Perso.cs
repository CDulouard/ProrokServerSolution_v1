using System;

namespace Exemple
{
    public class Perso
    {
        protected string _name;
        protected int _age;
        public static string espece = "humain";


        public Perso(string name, int age)
        {
            this._name = name;
            this._age = age;
        }

        public Perso(string name)
        {
            this._name = name;
            this._age = 10;
        }

        public void SePresenter()
        {
            Console.WriteLine("Bonjour je m'appel " + _name + " et j'ai " + _age.ToString() + " ans et je suis un " +
                              espece);
        }

        public void SetAge(int age)
        {
            if (age >= 0)
            {
                this._age = age;
            }
        }

        public static void SetEspece(string espece)
        {
            Perso.espece = espece;
        }
    }
}