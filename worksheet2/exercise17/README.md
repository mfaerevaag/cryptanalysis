Exercise 15
===========

By using a MD5 reduction function `f`, outputting a key-size of 20 bits, we
have generated a Rainbow table with `2^16` chains, each with a length
of `2^8`. That is, by iterating the reduction function 256 times.

    f = Min 20 bits of (MD5(s) ^ i)

## Coverage

In total our implementation covers ca. **1034904** of the total
ca. **1048576** (2^20), which gives us about **98.8 %** coverage.
This is a phenomenal improvement from the Hellman's at around 30 %!

## Count vs *i*

We have kept track of how many points of the total key-space we
actually have covered after *i* calls to the reduction function `f`:

<center>
<table>
    <tr>
        <td><b>Covered</b></td>
        <td><b><i>i</b></i></td>
    </tr>
    <tr>
        <td>0</td>
        <td>255</td>
    </tr>
    <tr>
        <td>5000</td>
        <td>645180</td>
    </tr>
    <tr>
        <td>10000</td>
        <td>836326</td>
    </tr>
    <tr>
        <td>15000</td>
        <td>916822</td>
    </tr>
    <tr>
        <td>20000</td>
        <td>959115</td>
    </tr>
    <tr>
        <td>25000</td>
        <td>983192</td>
    </tr>
    <tr>
        <td>30000</td>
        <td>999148</td>
    </tr>
    <tr>
        <td>35000</td>
        <td>1009589</td>
    </tr>
    <tr>
        <td>40000</td>
        <td>1017355</td>
    </tr>
    <tr>
        <td>45000</td>
        <td>1023006</td>
    </tr>
    <tr>
        <td>50000</td>
        <td>1027086</td>
    </tr>
    <tr>
        <td>55000</td>
        <td>1030204</td>
    </tr>
    <tr>
        <td>60000</td>
        <td>1032709</td>
    </tr>
    <tr>
        <td>65000</td>
        <td>1034740</td>
    </tr>
</table>
</center>

These results can be found in `covered-points.csv`

Here is a graph showing the results:

<center>
    ![Count vs i](graph.png)
</center>
