<?xml version="1.0"?>

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

   <xsl:template match="/">

      <html xmlns="http://www.w3.org/1999/xhtml">
         <head>
            <title><xsl:value-of select="umsatz/firma/name"/></title>
            <link rel="stylesheet" type="text/css" href="style01.css"/>
         </head>
         <body>
            <h1>Jahresumsätze der <xsl:value-of select="umsatz/firma/name"/></h1>
            <table align="center">
               <caption>Umsätze von <xsl:value-of select="umsatz/jahre/jahr[1]/@jahr"/>
                        bis <xsl:value-of select="umsatz/jahre/jahr[last()]/@jahr"/></caption>
               <thead>
                  <tr>
                     <th>Jahr</th>
                     <th style="background-color:#ccffff"><xsl:value-of select="umsatz/firma/sparten/sparte[1]"/></th>
                     <th style="background-color:#ffcccc"><xsl:value-of select="umsatz/firma/sparten/sparte[2]"/></th>
                     <th style="background-color:#ccccff"><xsl:value-of select="umsatz/firma/sparten/sparte[3]"/></th>
                     <th>Summe</th>
                  </tr>
               </thead>
               <tbody>
                  <xsl:for-each select="umsatz/jahre/jahr">
                     <tr>
                        <td><xsl:value-of select="@jahr"/></td>
                        <td><xsl:value-of select="petro"/></td>
                        <td><xsl:value-of select="pharma"/></td>
                        <td><xsl:value-of select="photo"/></td>
                        <td><xsl:value-of select="petro + photo + pharma"/></td>
                     </tr>
                  </xsl:for-each>
               </tbody>
            </table>

         </body>
      </html>

   </xsl:template>

</xsl:stylesheet>
