<?xml version="1.0" encoding="ISO-8859-1"?>
<StyledLayerDescriptor version="1.0.0" xmlns="http://www.opengis.net/sld" xmlns:gml="http://www.opengis.net/gml" xmlns:ogc="http://www.opengis.net/ogc" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.opengis.net/sld http://schemas.opengis.net/sld/1.0.0/StyledLayerDescriptor.xsd">
  <NamedLayer>
    <Name>data_pob_servicios_alumbrado_elect</Name>
    <UserStyle>
      <FeatureTypeStyle>

        <Rule>

          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>cod_rv_sel</ogc:PropertyName>
              <ogc:Literal>5</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <Name>60.0% - 100.0%</Name>
          <PolygonSymbolizer>
            <Fill>
              <CssParameter name="fill">#cd171f</CssParameter>
            </Fill>
            <Stroke>
              <CssParameter name="stroke">#4d4d4d</CssParameter>
              <!--CssParameter name="stroke-opacity">0.5</CssParameter-->
              <CssParameter name="stroke-width">1</CssParameter>
            </Stroke>
          </PolygonSymbolizer>
          <TextSymbolizer>
            <Label><ogc:PropertyName>nom_dist</ogc:PropertyName></Label>
            <Font>
              <CssParameter name="font-family">Arial</CssParameter>
              <CssParameter name="font-size">8</CssParameter>
            </Font>
            <LabelPlacement>
              <PointPlacement>
                <AnchorPoint>
                  <AnchorPointX>0.5</AnchorPointX>
                  <AnchorPointY>0.5</AnchorPointY>
                </AnchorPoint>
              </PointPlacement>
            </LabelPlacement>
            <Fill>
              <CssParameter name="fill">#000000</CssParameter>
            </Fill>
          </TextSymbolizer>
        </Rule>
        
        <Rule>

          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>cod_rv_sel</ogc:PropertyName>
              <ogc:Literal>4</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <Name>40.0% - 59.9%</Name>
          <PolygonSymbolizer>
            <Fill>
              <CssParameter name="fill">#ee6645</CssParameter>
            </Fill>
            <Stroke>
              <CssParameter name="stroke">#4d4d4d</CssParameter>
              <!--CssParameter name="stroke-opacity">0.5</CssParameter-->
              <CssParameter name="stroke-width">1</CssParameter>
            </Stroke>
          </PolygonSymbolizer>
          <TextSymbolizer>
            <Label><ogc:PropertyName>nom_dist</ogc:PropertyName></Label>
            <Font>
              <CssParameter name="font-family">Arial</CssParameter>
              <CssParameter name="font-size">8</CssParameter>
            </Font>
            <LabelPlacement>
              <PointPlacement>
                <AnchorPoint>
                  <AnchorPointX>0.5</AnchorPointX>
                  <AnchorPointY>0.5</AnchorPointY>
                </AnchorPoint>
              </PointPlacement>
            </LabelPlacement>
            <Fill>
              <CssParameter name="fill">#000000</CssParameter>
            </Fill>
          </TextSymbolizer>
        </Rule>
        
         <Rule>

          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>cod_rv_sel</ogc:PropertyName>
              <ogc:Literal>3</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <Name>20.0% - 39.9%</Name>
          <PolygonSymbolizer>
            <Fill>
              <CssParameter name="fill">#f59678</CssParameter>
            </Fill>
            <Stroke>
              <CssParameter name="stroke">#8c8c8c</CssParameter>
              <!--CssParameter name="stroke-opacity">0.5</CssParameter-->
              <CssParameter name="stroke-width">1</CssParameter>
            </Stroke>
          </PolygonSymbolizer>
          <TextSymbolizer>
            <Label><ogc:PropertyName>nom_dist</ogc:PropertyName></Label>
            <Font>
              <CssParameter name="font-family">Arial</CssParameter>
              <CssParameter name="font-size">8</CssParameter>
            </Font>
            <LabelPlacement>
              <PointPlacement>
                <AnchorPoint>
                  <AnchorPointX>0.5</AnchorPointX>
                  <AnchorPointY>0.5</AnchorPointY>
                </AnchorPoint>
              </PointPlacement>
            </LabelPlacement>
            <Fill>
              <CssParameter name="fill">#000000</CssParameter>
            </Fill>
          </TextSymbolizer>
        </Rule>

        
        <Rule>

          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>cod_rv_sel</ogc:PropertyName>
              <ogc:Literal>2</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <Name>10.0% - 19.9%</Name>
          <PolygonSymbolizer>
            <Fill>
              <CssParameter name="fill">#fcc878</CssParameter>
            </Fill>
            <Stroke>
              <CssParameter name="stroke">#8c8c8c</CssParameter>
              <!--CssParameter name="stroke-opacity">0.5</CssParameter-->
              <CssParameter name="stroke-width">1</CssParameter>
            </Stroke>
          </PolygonSymbolizer>
          <TextSymbolizer>
            <Label><ogc:PropertyName>nom_dist</ogc:PropertyName></Label>
            <Font>
              <CssParameter name="font-family">Arial</CssParameter>
              <CssParameter name="font-size">8</CssParameter>
            </Font>
            <LabelPlacement>
              <PointPlacement>
                <AnchorPoint>
                  <AnchorPointX>0.5</AnchorPointX>
                  <AnchorPointY>0.5</AnchorPointY>
                </AnchorPoint>
              </PointPlacement>
            </LabelPlacement>
            <Fill>
              <CssParameter name="fill">#000000</CssParameter>
            </Fill>
          </TextSymbolizer>
        </Rule>
        
        
        <Rule>

          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>cod_rv_sel</ogc:PropertyName>
              <ogc:Literal>1</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <Name>0.0% - 9.9%</Name>
          <PolygonSymbolizer>
            <Fill>
              <CssParameter name="fill">#ffe7dd</CssParameter>
            </Fill>
            <Stroke>
              <CssParameter name="stroke">#8c8c8c</CssParameter>
              <!--CssParameter name="stroke-opacity">0.5</CssParameter-->
              <CssParameter name="stroke-width">1</CssParameter>
            </Stroke>
          </PolygonSymbolizer>
          <TextSymbolizer>
            <Label><ogc:PropertyName>nom_dist</ogc:PropertyName></Label>
            <Font>
              <CssParameter name="font-family">Arial</CssParameter>
              <CssParameter name="font-size">8</CssParameter>
            </Font>
            <LabelPlacement>
              <PointPlacement>
                <AnchorPoint>
                  <AnchorPointX>0.5</AnchorPointX>
                  <AnchorPointY>0.5</AnchorPointY>
                </AnchorPoint>
              </PointPlacement>
            </LabelPlacement>
            <Fill>
              <CssParameter name="fill">#000000</CssParameter>
            </Fill>
          </TextSymbolizer>
        </Rule>
        

      </FeatureTypeStyle>
    </UserStyle>
  </NamedLayer>
</StyledLayerDescriptor>