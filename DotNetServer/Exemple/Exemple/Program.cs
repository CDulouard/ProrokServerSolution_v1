using System;

namespace Exemple
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            Perso.SetEspece("lapin");
            Perso jean = new Perso("jean", 20);
            jean.SePresenter();
            jean.SetAge(-10);
            jean.SePresenter();
            jean.SetAge(10);
            jean.SePresenter();

            Perso robert = new Perso("Robert");
            robert.SePresenter();
            Console.WriteLine(Perso.espece);
            
            Employe pierre = new Employe("Pierre", 30, "Boulanger");
            pierre.ChangerDeMetier("Livreur");
            pierre.SePresenter();
            
            
        }
    }
}