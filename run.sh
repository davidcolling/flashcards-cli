cp $1 $DOCKER/flashcards-python/cpbox/cards.txt
docker run -it --rm --mount type=bind,src="$DOCKER/flashcards-python/cpbox",dst="/cpbox" flashcards-python python3 /root/flashcards.py 
rm $DOCKER/flashcards-python/cpbox/cards.txt
