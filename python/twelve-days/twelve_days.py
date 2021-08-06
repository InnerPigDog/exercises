DAY = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh",
       "eighth", "ninth", "tenth", "eleventh", "twelfth"]

ENUMERATION = [
    "twelve Drummers Drumming, ",
    "eleven Pipers Piping, ",
    "ten Lords-a-Leaping, ",
    "nine Ladies Dancing, ",
    "eight Maids-a-Milking, ",
    "seven Swans-a-Swimming, ",
    "six Geese-a-Laying, ",
    "five Gold Rings, ",
    "four Calling Birds, ",
    "three French Hens, ",
    "two Turtle Doves, and ",
    "a Partridge in a Pear Tree.",
]


def recite(start_verse: int, end_verse: int) -> list[str]:

    return [f"On the {DAY[i-1]} day of Christmas my true love gave to me: "
            + "".join(ENUMERATION[12-i:])
            for i in range(start_verse, end_verse+1)]
