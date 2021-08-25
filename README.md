# zsh-history-clear
Clear .zsh_history file. Remove older command and other stuff, increase opening speed of zsh

All settings for this script are on top of the file.
You can disable filter criteria simply by setting it to `None`

| Filter | Type | Description |
|-----------------------|-----------------|-----------------------------------------------------------|
| OLDER_THAN | number | Remove all command logger x days ago. |
| LESS_THAN | number | Remove all command lower than x chars. |
| GREATER_THAN | number | Remove all command greater than x chars. |
| START_WITH | array of string | Remove all command start with one of the string in array. |
| REMOVE_WITH_EXCEPTION | boolean | Remove all lines that cause exception. |
| REMOVE_DUPLICATE | boolean | Remove all duplicate commands. |
