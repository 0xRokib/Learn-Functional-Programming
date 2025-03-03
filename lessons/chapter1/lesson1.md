# What Is Functional Programming?

Functional programming is a style (or "paradigm") of programming where we compose functions instead of mutating state (updating the value of variables).

Functional programming is more about declaring **what** you want to happen, rather than **how** you want it to happen.

## Imperative vs. Functional Programming

### Imperative Code Example:

```python
car = create_car()
car.add_gas(10)
car.clean_windows()
```

### Functional Code Example:

```python
return clean_windows(add_gas(create_car()))
```

In the functional example, the value of `car` is never changed. Instead, functions return new values with each transformation.

---

## Immutability

In FP, we strive to make data **immutable**. Once a value is created, it cannot be changed.

### Why Immutability Matters?

Immutable data is easier to reason about because you can be sure that a value hasn't changed since it was created.

### Example:

#### Lists (Mutable):

```python
ages = [16, 21, 30]
ages.append(80)  # [16, 21, 30, 80]
```

#### Tuples (Immutable):

```python
ages = (16, 21, 30)
more_ages = (80,)
all_ages = ages + more_ages  # (16, 21, 30, 80)
```

---

## Declarative Programming

Functional programming aims to be **declarative** — describing what should be done, not how.

### Example:

#### Declarative Styling (CSS):

```css
button {
  color: red;
}
```

#### Imperative Styling (Tkinter in Python):

```python
from tkinter import *
master = Tk()
master.geometry("200x100")
button = Button(master, text="Submit", fg="red").pack()
master.mainloop()
```

---

## Functional Programming and Math

Functional programming is often popular with developers who have a strong mathematical background.

### Average Calculation

#### Imperative Code:

```python
def get_average(nums):
    total = 0
    for num in nums:
        total += num
    return total / len(nums)
```

#### Functional Code:

```python
def get_average(nums):
    return sum(nums) / len(nums)
```

---

## Functions vs. Classes

### When to Use Functions?

If you're unsure, **default to functions**.

Use classes when you need something long-lived and stateful, like:

- Video games
- Simulations
- GUIs

### Classes Encourage:

- Hierarchical collections of objects
- Bundling data and behavior together

### Functions Encourage:

- Data transformations
- Stateless operations

---

## Debugging in FP

Debugging functional code can be challenging due to one-liners.

### Example:

#### Difficult to Debug:

```python
def get_player_position(position, velocity, friction, gravity):
    return calc_gravity(calc_friction(calc_move(position, velocity), friction), gravity)
```

#### Easier to Debug:

```python
def get_player_position(position, velocity, friction, gravity):
    moved = calc_move(position, velocity)
    slowed = calc_friction(moved, friction)
    final = calc_gravity(slowed, gravity)
    print(f"position: {position}, velocity: {velocity}, friction: {friction}, gravity: {gravity}")
    print(f"moved: {moved}, slowed: {slowed}, final: {final}")
    return final
```

---

## Functional Programming vs. Object-Oriented Programming

FP and OOP are not always at odds.

| Feature       | OOP | FP  |
| ------------- | --- | --- |
| Inheritance   | ✅  | ❌  |
| Encapsulation | ✅  | ✅  |
| Polymorphism  | ✅  | ✅  |
| Abstraction   | ✅  | ✅  |

### Best Practice

Combine the best ideas from both paradigms when appropriate.

---

## Conclusion

Functional programming is a powerful paradigm that encourages immutability, declarative code, and pure functions. By understanding both FP and OOP, you can write more maintainable and bug-free software.
