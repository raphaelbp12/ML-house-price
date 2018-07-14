def julienFeatSimp(train):
    # 1* Simplifications of existing features
    train["SimplOverallQual"] = train.OverallQual.replace({1 : 1, 2 : 1, 3 : 1, # bad
                                                        4 : 2, 5 : 2, 6 : 2, # average
                                                        7 : 3, 8 : 3, 9 : 3, 10 : 3 # good
                                                        })
    train["SimplOverallCond"] = train.OverallCond.replace({1 : 1, 2 : 1, 3 : 1, # bad
                                                        4 : 2, 5 : 2, 6 : 2, # average
                                                        7 : 3, 8 : 3, 9 : 3, 10 : 3 # good
                                                        })
    train["SimplPoolQC"] = train.PoolQC.replace({1 : 1, 2 : 1, # average
                                                3 : 2, 4 : 2 # good
                                                })
    train["SimplGarageCond"] = train.GarageCond.replace({1 : 1, # bad
                                                        2 : 1, 3 : 1, # average
                                                        4 : 2, 5 : 2 # good
                                                        })
    train["SimplGarageQual"] = train.GarageQual.replace({1 : 1, # bad
                                                        2 : 1, 3 : 1, # average
                                                        4 : 2, 5 : 2 # good
                                                        })
    train["SimplFireplaceQu"] = train.FireplaceQu.replace({1 : 1, # bad
                                                        2 : 1, 3 : 1, # average
                                                        4 : 2, 5 : 2 # good
                                                        })
    train["SimplFireplaceQu"] = train.FireplaceQu.replace({1 : 1, # bad
                                                        2 : 1, 3 : 1, # average
                                                        4 : 2, 5 : 2 # good
                                                        })
    train["SimplFunctional"] = train.Functional.replace({1 : 1, 2 : 1, # bad
                                                        3 : 2, 4 : 2, # major
                                                        5 : 3, 6 : 3, 7 : 3, # minor
                                                        8 : 4 # typical
                                                        })
    train["SimplKitchenQual"] = train.KitchenQual.replace({1 : 1, # bad
                                                        2 : 1, 3 : 1, # average
                                                        4 : 2, 5 : 2 # good
                                                        })
    train["SimplHeatingQC"] = train.HeatingQC.replace({1 : 1, # bad
                                                    2 : 1, 3 : 1, # average
                                                    4 : 2, 5 : 2 # good
                                                    })
    train["SimplBsmtFinType1"] = train.BsmtFinType1.replace({1 : 1, # unfinished
                                                            2 : 1, 3 : 1, # rec room
                                                            4 : 2, 5 : 2, 6 : 2 # living quarters
                                                            })
    train["SimplBsmtFinType2"] = train.BsmtFinType2.replace({1 : 1, # unfinished
                                                            2 : 1, 3 : 1, # rec room
                                                            4 : 2, 5 : 2, 6 : 2 # living quarters
                                                            })
    train["SimplBsmtCond"] = train.BsmtCond.replace({1 : 1, # bad
                                                    2 : 1, 3 : 1, # average
                                                    4 : 2, 5 : 2 # good
                                                    })
    train["SimplBsmtQual"] = train.BsmtQual.replace({1 : 1, # bad
                                                    2 : 1, 3 : 1, # average
                                                    4 : 2, 5 : 2 # good
                                                    })
    train["SimplExterCond"] = train.ExterCond.replace({1 : 1, # bad
                                                    2 : 1, 3 : 1, # average
                                                    4 : 2, 5 : 2 # good
                                                    })
    train["SimplExterQual"] = train.ExterQual.replace({1 : 1, # bad
                                                    2 : 1, 3 : 1, # average
                                                    4 : 2, 5 : 2 # good
                                                    })

    return train