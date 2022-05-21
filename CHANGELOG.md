# Changelog

<!--next-version-placeholder-->

## v0.3.1 (2022-05-21)
### Fix
* Make runner available from base package ([`5c59466`](https://github.com/aadhithya/rajiniPP/commit/5c59466ff0b48d064f7649d73bd883203ea4da22))
* Add init files to submodules ([`53d6378`](https://github.com/aadhithya/rajiniPP/commit/53d6378c47af8108d35a355f2c976c0f72c8f0aa))

### Documentation
* Add issue and pr templates ([`1deabc4`](https://github.com/aadhithya/rajiniPP/commit/1deabc4c60572b0fb2dad3407f90f5ef91ecd704))
* Add contributing code of conduct guidelines ([`b547186`](https://github.com/aadhithya/rajiniPP/commit/b547186df1dfa31412014973407a4e84d9883e90))

## v0.3.0 (2022-05-16)
### Feature
* **ProgramParser:** Add support for functions ([`d95a3f9`](https://github.com/aadhithya/rajiniPP/commit/d95a3f9dc01c276316fb8fb43e456ee5b8daee8f))
* **FunctionParser:** Add parser to support functions ([`ab53faa`](https://github.com/aadhithya/rajiniPP/commit/ab53faaca610ad8ef852fb1c6ad062ac335fd136))
* **AtomParser:** Add new production for function name ([`28c9370`](https://github.com/aadhithya/rajiniPP/commit/28c9370764aa6c35bbd7deaf1918f60baaed0e7f))
* **ReturnException:** Add exception to handle return statements ([`cc99f7c`](https://github.com/aadhithya/rajiniPP/commit/cc99f7c40d63b6d1aa664a3930a538b4c525d605))
* **control.py:** Add node classes to support functions ([`8e90d1e`](https://github.com/aadhithya/rajiniPP/commit/8e90d1e312e3c19a88a3fe8c680e999631a8a0ae))
* **blocks.py:** Add classes to handle program and functions blocks ([`d2ddf15`](https://github.com/aadhithya/rajiniPP/commit/d2ddf15171b64ef1ff9ec2931d7bde9a92738426))
* **__rajiniworld__.py:** Add __functions__ to store functions ([`efacd36`](https://github.com/aadhithya/rajiniPP/commit/efacd36e248d0e35619535e6d544460684168ec5))
* **token.yml:** Enable tokens for functions ([`718ca1c`](https://github.com/aadhithya/rajiniPP/commit/718ca1cfe84ce0016b72592add16760f3921949c))

### Documentation
* **examples:** Add example program for functions ([`1eb0ab2`](https://github.com/aadhithya/rajiniPP/commit/1eb0ab2e8102c9440c6b06b0e1efe3728c1a936c))
* **examples:** Add example for functions ([`505813b`](https://github.com/aadhithya/rajiniPP/commit/505813b0be79085997d9016816286310d5aec3f6))
* **README.md:** Update readme ([`b23a777`](https://github.com/aadhithya/rajiniPP/commit/b23a777358a8a926526c29ac8b4a66f5d775a771))

## v0.2.0 (2022-05-16)
### Feature
* **flow_parser.py:** Add support for while loops and break statement ([`67feeed`](https://github.com/aadhithya/rajiniPP/commit/67feeedc2582e238eaa180dea7eb57b8c5532ca2))
* **exceptions.py:** Add exception to handle break statements ([`89cb89f`](https://github.com/aadhithya/rajiniPP/commit/89cb89f12140f686a3596731a9de97540ec516d2))
* **token.yml:** Allow while loop and break tokens ([`bb4ee89`](https://github.com/aadhithya/rajiniPP/commit/bb4ee895588ec4896a832d6d0e28d8aebca74620))
* **control.py:** Support while loop and break nodes ([`2011db1`](https://github.com/aadhithya/rajiniPP/commit/2011db19520d0a7b764c13b3d1df28217e08f709))
* **ParserBase:** Add support for for loops ([`70a49d3`](https://github.com/aadhithya/rajiniPP/commit/70a49d3427fd261f48db420d684a79ec0a553ef4))
* **flow_parser.py:** Add parser to support loops, rename cond_parser to flow_parser ([`78cc1da`](https://github.com/aadhithya/rajiniPP/commit/78cc1da823015655e0f071f4ebf81006f74b2c6d))
* **ForLoop:** Add node to support for loops ([`7c951eb`](https://github.com/aadhithya/rajiniPP/commit/7c951ebcc3640c9c7ab290672b8f97586af6f9be))
* **token.yml:** Enable for loop ([`371ebbe`](https://github.com/aadhithya/rajiniPP/commit/371ebbe313fa8b4cae1b0be66e085885ed2c7e29))
* **__main__.py:** Add support for rajini++ shell ([`eaee4c9`](https://github.com/aadhithya/rajiniPP/commit/eaee4c96890d5ad297338c28d6d3f717c18fd90a))
* **RppRunner:** Add eval function to evaluate statements, refactor code ([`38cb454`](https://github.com/aadhithya/rajiniPP/commit/38cb4549e38a446f6a27f5eb2f2e0a09be2253c5))
* **parser.py:** Add line parser to parse statements, refactor code ([`24263bc`](https://github.com/aadhithya/rajiniPP/commit/24263bcf3a10514dbe4b02197e870885fa740f72))
* **Expression:** Add expression node ([`f69ffc0`](https://github.com/aadhithya/rajiniPP/commit/f69ffc0c40cf2f4c390b501dcd0ae64bb6283b6b))
* **runner.py:** Replace api with runner and runner class ([`64ba844`](https://github.com/aadhithya/rajiniPP/commit/64ba844f10644c49952d19e60d22d40fd645410b))
* **ConditionalParser:** Add support for if-else statements ([`2a219dc`](https://github.com/aadhithya/rajiniPP/commit/2a219dc48370a8019c6b108318fd88131577220d))
* **IfElseCondition:** Add node to interpret if-else statements ([`8ae2192`](https://github.com/aadhithya/rajiniPP/commit/8ae2192a081d9f9128a105b56438feaefb7d6a33))

### Fix
* **__main__.py:** Fix logger levels ([`a0000b3`](https://github.com/aadhithya/rajiniPP/commit/a0000b34568960bc738dcd5ced6c9a1f98961817))
* **AtomParser:** Add new production rule to support loops ([`ab91aad`](https://github.com/aadhithya/rajiniPP/commit/ab91aad0fe9961129946945cc50546606331a492))
* **base.py:** __vars__ now store the evaluated value of the variable instead of the node ([`75936c7`](https://github.com/aadhithya/rajiniPP/commit/75936c7d83b1e30cc23efaa93f41865823b0600f))
* **__main__.py:** Fix shell false bug ([`5efcd49`](https://github.com/aadhithya/rajiniPP/commit/5efcd4925dc6cf97bbebe83b974ff9c7d5491c21))
* **token.yml:** Enable ELSE_COND ([`bcb55aa`](https://github.com/aadhithya/rajiniPP/commit/bcb55aaac6c95b20c605375c9ac2d5cd92937b75))

### Documentation
* **LANG.md:** Move language specification to wiki ([`94d2aee`](https://github.com/aadhithya/rajiniPP/commit/94d2aeea5a6d13135872b2ff1b9893ded2552e52))
* **while_loop.rpp:** Add while loop with break statement example ([`144204f`](https://github.com/aadhithya/rajiniPP/commit/144204f0bc54fe4b1b6cf8a055741b2b64e332e7))
* **examples:** Add for loop and fizzbuzz examples ([`7442ffc`](https://github.com/aadhithya/rajiniPP/commit/7442ffcddab5a05fea3f6b1c7bbe9138391a191b))
* **README.md:** Update readme ([`280e0eb`](https://github.com/aadhithya/rajiniPP/commit/280e0eb6f9c2ebde47a7ba93d562b4ac22bca8d5))
* **examples:** Add example program for if-else statements ([`b463b52`](https://github.com/aadhithya/rajiniPP/commit/b463b52210e0a5156f6a1598d38b6af3cbbc4c54))
* **README.md:** Update readme ([`9273dc9`](https://github.com/aadhithya/rajiniPP/commit/9273dc9424a37748a62e0c9dbf39fef740668367))
* **README.md:** Fix formatting ([`e1e6567`](https://github.com/aadhithya/rajiniPP/commit/e1e65673ec7e3adc78ed19015d8274d264e13832))
* **README.md:** Update installation instructions ([`594c808`](https://github.com/aadhithya/rajiniPP/commit/594c8089dffef63a32f85ba90bdf77713a4145f2))

## v0.1.2 (2022-05-14)
### Fix
* **release.yml:** Add fetch depth parameter ([`cdd7108`](https://github.com/aadhithya/rajiniPP/commit/cdd71080a8e6948279eec61efc67b46108097210))
* **release.yml:** Hopefully fix token access issue ([`a8e53ec`](https://github.com/aadhithya/rajiniPP/commit/a8e53ec14eb5a2dd6d07dace1bd66ef215f57d05))

## v0.1.1 (2022-05-14)
### Fix
* **release.yml:** Fix github token name ([`14164ed`](https://github.com/aadhithya/rajiniPP/commit/14164ed3928079105849f3c3790a0087d1fd5ce9))

## v0.1.0 (2022-05-14)
### Feature
* **api.py:** Add api ([`f559d12`](https://github.com/aadhithya/rajiniPP/commit/f559d122bc3abb0616457bdb85ec1c5ef8451036))
