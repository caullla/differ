# differ

Display diff between two lines.

Example:
```
old:    "same_prefix_12533_same_suffix"
new:    "same_prefix23123_same_suffix"
result: "same_prefix(_)[23]12(53)3_same_suffix"
```
* "()" - contains only in old version
* "[]" contains only in new version

Logic:
```
                   'same_prefix_123_same_suffix'
                   'same2prefix_1233_same_suffix'
                                |
                         '3_same_suffix'
              'same_prefix_12'      ''
              'same2prefix_123'     ''
                      |
                  'prefix_12'
            'same_'        ''
            'same2'        '3'
               |            |
             'same'       [3]
            ''     '_'
            ''     '2'
                    |
                 (_)[2]

'same' '(_)' '[2]' 'prefix_12' '[3]' '3_same_suffix'
```
