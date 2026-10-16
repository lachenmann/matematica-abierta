-- CPM: preserve semantic anchors and make all solutions visible in print.
local envs={def='definition',thm='theorem',lem='lemma',prp='proposition',cor='corollary',exm='example'}
local chapter=(PANDOC_STATE.input_files[1] or ''):match('c(%d+)%.md') or '00'
local math_index=0
function Header(el)
  if not el.identifier:match('^sec%-t1%-') then el.identifier='c'..chapter..'-'..el.identifier end
  if pandoc.utils.stringify(el.content):match('^Soluciones') then
    local lines=el.level<=3 and 12 or 8
    return {pandoc.RawBlock('latex','\\Needspace{'..lines..'\\baselineskip}'),el}
  end
  return el
end
function Div(el)
  local kind=el.identifier:match('^(%a+)%-t1%-')
  local out=pandoc.List()
  local opening,closing
  if envs[kind] then
    opening='\\begin{'..envs[kind]..'}\\label{'..el.identifier..'}'
    closing='\\end{'..envs[kind]..'}'
  elseif kind=='exr' or kind=='sol' then
    opening='\\par\\medskip\\Needspace{4\\baselineskip}\\phantomsection\\label{'..el.identifier..'}'
    closing='\\par\\medskip'
  elseif #el.classes>0 then
    opening='\\begin{cpmnote}'
    closing='\\end{cpmnote}'
    local title=el.attributes.title
    if title then
      opening=opening..'\n'..pandoc.write(pandoc.Pandoc({pandoc.Para({pandoc.Strong(pandoc.read(title,'markdown').blocks[1].content)})}),'latex')
    end
  else
    opening=el.identifier~='' and '\\phantomsection\\label{'..el.identifier..'}' or ''
    closing=''
  end
  out:insert(pandoc.RawBlock('latex',opening))
  out:extend(el.content)
  out:insert(pandoc.RawBlock('latex',closing))
  return out
end
function Math(el)
  if el.mathtype=='DisplayMath' then
    math_index=math_index+1
    local text=el.text:gsub('^%s+',''):gsub('%s+$',''):gsub('\n%s*\n','\n')
    return pandoc.RawInline('latex','\\begin{cpmath}{'..math_index..'}\n'..text..'\n\\end{cpmath}')
  end
end
