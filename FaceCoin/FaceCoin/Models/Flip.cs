using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;

namespace FaceCoin.Models
{
    public class Flip
    {
        public string lado { get; set; }
     
        public string Rolar()
        {
            int ladoSorteado = new Random().Next(2);
            lado = ladoSorteado == 0 ? "cara" : "coroa";
            return lado;
        }
        public string Rolar(string ladoEscolhido) 
        {
            int ladoSorteado = new Random().Next(2);
            lado = ladoSorteado == 0 ? "cara" : "coroa";
            string resultado = lado == ladoEscolhido ?
                $"Parabéns, você pediu {ladoEscolhido} e deu {lado}" :
                $"Meus pesos, você pediu {ladoEscolhido} e deu {lado}";
            return resultado;
        }


    }
}