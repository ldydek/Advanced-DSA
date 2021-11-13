# Do implementacji algorytmu wyznaczającego wszystkie przecięcia zbioru odcinków na płaszczyźnie będziemy potrzebowali
# dwóch drzew czerwono-czarnych - kolejka zdarzeń oraz struktura stanu. Pierwsza z nich będzie służyła do zwrócenia
# punktu, do którego ma się udać miotła i wykonać pewne operacje. Drugie drzewo przechowuje odcinki, które na chwilę
# obecną przecinają się z miotłą. W kolejce zdarzeń możemy przechowywać trójki postaci (x, y, a), gdzie x i y to
# współrzędne punktu, a a informuje nas czy jest to lewy czy prawy koniec odcinka, czy może punkt przecięcia.
# (być może jeszcze nr tego odcinka, więc będą to czwórki)???. W każdym
# przypadku wymaga to innej operacji na strukturze stanu. Warto zauważyć, iż implementacja kolejki zdarzeń jako
# kopca binarnego nie jest dobrym pomysłem, ponieważ podczas dodawania nowych punktów przecięć do tej kolejki zdarzeń,
# musimy przy okazji sprawdzić, czy ten punkt już się tam znajduje (w kopcu wymagałoby to czasu O(n), natomiast
# w drzewie czerwono-czarnym już tylko O(log n)).
# A co jeśli w kolejce zdarzeń przechowywać krotki postaci (a, b), gdzie a to nr odcinka a b to informacja o jego
# lewym bądź prawym końcu (True, False) a ewentualne punkty przecięcia jako (x, y, a, b) gdzie y to liczba a nie False
# lub True a a i b to nry odcinków, które sie przecinaja w tym punkcie. W strukturze stanu możemy przechowywać tylko
# klucze jako liczby naturalne reprezentujące nr odcinka. Na sam koniec potrzebuje tylko jeszcze dobrego algorytmu
# wyznaczjącego punkt przecięcia dwóch odcinków, o ile się przecinają. Dla danej współrzędnej x odcinki zaczynające się
# mają pierwszeństwo przed kończącymi się, aby wykryć możliwe przecięcie!

