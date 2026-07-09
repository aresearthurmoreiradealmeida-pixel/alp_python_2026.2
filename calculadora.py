{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMRv0mx3F9l3TGB4kc648+s",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/aresearthurmoreiradealmeida-pixel/alp_python_2026.2/blob/main/calculadora.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "ec7RNWLxANVT"
      },
      "outputs": [],
      "source": [
        "while True:\n",
        "  opcao = int(input(\n",
        "  \"\"\"---Calculadora de números reais---\n",
        "\n",
        "0.Sair\n",
        "1.Soma\n",
        "2.Subtração\n",
        "3.Multiplicação\n",
        "4.Divisão\n",
        "\n",
        "Digite uma opção (0/1/2/3/4): \"\"\"))\n",
        "\n",
        "  if opcao == 0:\n",
        "    print(\"Programa encerrado\")\n",
        "    break\n",
        "  elif opcao > 4:\n",
        "    print(\"Opção inválida\")\n",
        "    continue\n",
        "\n",
        "  numero1 = float(input(\"Digite o primeiro número: \"))\n",
        "  numero2 = float(input(\"Digite o segundo número: \"))\n",
        "\n",
        "  if opcao == 1:\n",
        "    print(f\"O resultado da soma é: {numero1 + numero2}\")\n",
        "  elif opcao == 2:\n",
        "    print(f\"O resultado da subtração é: {numero1 - numero2}\")\n",
        "  elif opcao == 3:\n",
        "    print(f\"O resultado da multiplicação é: {numero1 * numero2}\")\n",
        "  elif opcao == 4:\n",
        "    if numero2 != 0:\n",
        "      print(f\"O resultado da divisão é: {numero1 / numero2}\")\n",
        "    else:\n",
        "      print(\"Erro, divisão por zero. Escolha outro número\")"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "8PXMgYCnQ6_h"
      }
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "lPnP1Rb8QYtz"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "ozWIGeXJO08c"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}