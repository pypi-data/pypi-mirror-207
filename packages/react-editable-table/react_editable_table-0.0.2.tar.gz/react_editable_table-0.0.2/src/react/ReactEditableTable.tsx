import React, { useState } from 'react';
import {
  Table,
  Input,
  createStyles,
  ScrollArea,
  Loader,
  Box,
  MantineProvider,
} from '@mantine/core';
import { useMutationObserver } from 'ahooks';
import { WidgetModel } from '@jupyter-widgets/base';
import { useModelMessenger, useModelState, WidgetModelContext } from './model';

const useStyles = createStyles({
  table: {
    borderRadius: 8,
    borderCollapse: 'initial',
    overflow: 'hidden',

    '& thead tr th': {
      height: 50,
      textAlign: 'left',
      padding: '0.4375rem 0.625rem',
    },
    '& thead tr th:nth-of-type(1)': {
      width: 140,
    },
    '& thead tr th:nth-of-type(2)': {
      width: 140,
    },
  },
});

interface WidgetProps {
  model: WidgetModel;
  loading?: boolean;
}

function ReactEditableTable(props: WidgetProps) {
  const [columns] = useModelState('columns');
  const [meta] = useModelState('meta');
  const [data, setData] = useModelState('data');
  const send = useModelMessenger();
  const { classes } = useStyles();
  const { loading } = props;

  const rows = data.map((item, index) => {
    return (
      <tr key={index}>
        {columns.map((c) => (
          <td key={c.header}>
            {c.editable ? (
              <Input
                type="text"
                defaultValue={item[c.accessor]}
                onBlur={(e: any) => {
                  const next = e.target.value;
                  if (item[c.accessor] !== next) {
                    const data = { ...item, [c.accessor]: e.target.value };
                    setData((prev) => {
                      prev[index] = data;
                    });

                    send({
                      type: 'cell-changed',
                      payload: {
                        row: data,
                        index,
                        meta,
                      },
                    });
                  }
                }}
              />
            ) : (
              item[c.accessor]
            )}
          </td>
        ))}
      </tr>
    );
  });

  return (
    <div>
      <ScrollArea mah={400}>
        <Box maw={600}>
          <Table cellSpacing={0} className={classes.table}>
            <thead>
              <tr>
                {columns.map((i) => (
                  <th key={i.header}>{i.header}</th>
                ))}
              </tr>
            </thead>
            <tbody>{rows}</tbody>
          </Table>
        </Box>
      </ScrollArea>

      {loading && (
        <Loader size="xs" sx={{ position: 'absolute', top: 5, right: 0 }} />
      )}
    </div>
  );
}

function withModelContext(Component: (props: WidgetProps) => JSX.Element) {
  return (props: WidgetProps) => {
    const [dark, setDark] = useState(
      () => document.body.dataset.jpThemeLight === 'false'
    );
    useMutationObserver(
      (mutationsList) => {
        mutationsList.forEach((i) => {
          if (i.attributeName === 'data-jp-theme-light') {
            setDark(document.body.dataset.jpThemeLight === 'false');
          }
        });
      },
      document.body,
      {
        attributes: true,
        subtree: false,
      }
    );

    return (
      <WidgetModelContext.Provider value={props.model}>
        <MantineProvider
          theme={{ colorScheme: dark ? 'dark' : 'light' }}
          withGlobalStyles
          withNormalizeCSS
        >
          <Component {...props} />
        </MantineProvider>
      </WidgetModelContext.Provider>
    );
  };
}

export default withModelContext(ReactEditableTable);
