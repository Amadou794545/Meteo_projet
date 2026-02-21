import pytest
import pandas as pd
from utils.ListeChaine import LinkedList, Node


def test_node_initialization():
    """Vérifie qu'un nœud est correctement créé."""
    data = pd.DataFrame({"temp": [20]})
    node = Node("Paris", data)
    assert node.station_name == "Paris"
    assert node.data.equals(data)
    assert node.next is None


def test_linked_list_append_first_element():
    """Vérifie l'ajout du tout premier élément (head)."""
    ll = LinkedList()
    data = pd.DataFrame({"temp": [25]})
    ll.append("Lyon", data)

    assert ll.head is not None
    assert ll.head.station_name == "Lyon"
    assert ll.head.next is None


def test_linked_list_append_multiple_elements():
    """Vérifie que les éléments s'ajoutent bien à la suite les uns des autres."""
    ll = LinkedList()
    ll.append("Station 1", pd.DataFrame({"val": [1]}))
    ll.append("Station 2", pd.DataFrame({"val": [2]}))
    ll.append("Station 3", pd.DataFrame({"val": [3]}))

    assert ll.head.station_name == "Station 1"
    assert ll.head.next.station_name == "Station 2"
    assert ll.head.next.next.station_name == "Station 3"
    assert ll.head.next.next.next is None


def test_linked_list_display(capsys):
    """Vérifie que la méthode display imprime bien les bonnes informations."""
    ll = LinkedList()
    # On utilise un DataFrame minimal car display appelle .head()
    df = pd.DataFrame({"col": [10, 20]})
    ll.append("Nice", df)

    ll.display()

    captured = capsys.readouterr()
    assert "Station: Nice" in captured.out
    # Note: data.head() dans un print affiche le formatage pandas
    assert "col" in captured.out