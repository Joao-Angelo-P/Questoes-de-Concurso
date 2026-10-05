/**
 * ALEGO – Assembleia Legislativa do Estado de Goiás
 * Concurso Público – Edital 01/2025
 * Prova Objetiva (Tarde) – Analista Legislativo – Desenvolvedor de Sistemas
 * Nível Superior – Tipo 1 – Branca
 *
 * Questão 48
 *
 * (Q3881433)
 *
 * No contexto do desenvolvimento de aplicações web, o JavaScript é uma
 * linguagem amplamente utilizada para implementar comportamentos dinâmicos
 * e interativos.
 *
 * Assinale a opção que apresenta a sintaxe correta para uma declaração
 * condicional if que verifica se a variável x é maior que 10 e, caso
 * verdadeiro, imprime "Maior que 10"
 *
 * (A) if x > 10 { console.log("Maior que 10"); }
 * (B) if (x >= 10) console.log("Maior que 10")
 * (C) if (x > 10) { console.log("Maior que 10"); } else { console.log("Menor ou igual a 10"); }
 * (D) if [x > 10] { console.log("Maior que 10"); }
 * (E) if (x > 10): { console.log("Maior que 10"); }
 *
 * Gabarito: C
 *
 * Comentário:
 * (A) Errada: a condição precisa estar entre parênteses.
 * (B) Errada: usa >= (maior ou igual), e o enunciado pede apenas "maior que".
 * (C) Correta: parênteses, operador > e blocos com chaves, incluindo o else.
 * (D) Errada: colchetes não delimitam condição em JavaScript.
 * (E) Errada: os dois-pontos (:) não fazem parte da sintaxe do if em JavaScript.
 */

// Resolução (alternativa C) – execute com: node questao-48.js
function verificar(x) {
  if (x > 10) {
    console.log("Maior que 10");
  } else {
    console.log("Menor ou igual a 10");
  }
}

verificar(15); // Maior que 10
verificar(10); // Menor ou igual a 10
verificar(5);  // Menor ou igual a 10
