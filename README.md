# web-caesar

This is a project for unit 2 of LaunchCode LC 101. A string of text is encrypted.

## Built With
* Python
* Flask
* HTML
* Bootstrap
* Heroku

## Functionality

Encryption - This program takes a string of text(text) and a number(rot) between 0 and 26 as input and returns a string with all of the alpha characters rotated the specified number of spaces to the right of the alphabet.

If a string is encrytped with a rotation of 13 and then encrypted again with a rotation of 13, the original message will appear because 13 + 13 = 26, the number of letters in the alphabet.

### examples
  * input - "The crow flies at midnight!" rotated by 13
  * output - "Gur pebj syvrf ng zvqavtug!"
  #
  * input - "Hello World!" rotated by 13
  * output - "Uryyb Jbeyq!"
