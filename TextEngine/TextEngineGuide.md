# Text Engine

### Normal Text
    This is normal text.

    [b]This is bold text.[b]

    [i]This is italic text.[i]

    [red]This is red.[red]

    [blue]This is blue.[blue]

    [green]This is green.[green]

    [gold]This is golden.[gold]

### Separators

    [box]
        Text stuff    
    [box]

    [box if="UserWeaponLevel(10)" if="UserUsingSword"]
        Text stuff    
    [box]
### Icon
    
    [Icon=SwordIcon]
    
### Calculation

    [eval="unit.GetStat('Damage')+3"]