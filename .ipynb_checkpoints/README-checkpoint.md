# pokerpy

*authors: dottorDav. & c1au6i0*
*date: April 2020.*

The aim of this project is to develop in `python` the classical power game, and in the process learn more about `python`,
probability and game theory and deep inside about our-selves and the meaning of life.

We are well aware that there are many other people that did it already (es: https://pypi.org/project/poker/), but again this is an exercise for us, and being able to take a peak at the work of someone else (probabily more experience then us) is even better.

# Possible structure of the game 

Here a tentative list of possible objects and classes and relative methods. It is language uspecific...

## deck

it contains the list of cards.

**Attributes:** 
* number of cards
* suits

**Methods**
* shuffle
* deal

**subclasses**
* card

## players

**Attributes:** 
* number of players
* human or PC
* IA level
* dealer or not
* seat (from the dealer)

**Methods**
* add or remove

**subclasses**
* player

## handranking

This should be a list of rules/raning of the different hands. This should be fleaxible to be able to allow variants of the game.

**Attributes:** 
* variant

## phase of the game

At what point of the game are we? this is weird. We got to think about this.

