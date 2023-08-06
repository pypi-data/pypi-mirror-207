# draw-isabelle

Quick visualization tool for nested Isabelle trees which are defined by the angle brace Isabelle syntax `⟨l, a, r⟩`.


## Install and usage

```console
$ pip install draw-isabelle
$ draw-isabelle '⟨⟨⟨⟨⟩, a, ⟨⟩⟩, a, ⟨⟨⟩, a, ⟨⟩⟩⟩, a, ⟨⟨⟩, a, ⟨⟩⟩⟩'
```

will output
```
          ________a___
         /            \
     ___a___          _a
    /       \        /  \
  _a        _a      ⟨⟩   ⟨⟩
 /  \      /  \
⟨⟩   ⟨⟩   ⟨⟩   ⟨⟩
```


## Contributing
Please open PR's with fixes and code improvements; could be cool to also support the Node/Leaf syntax or maybe other useful structures.

Code is also pretty untested so please LMK with breaking examples.

Might also make sense to code the ASCII tree representation in this repo to remove the binarytree dependency.
