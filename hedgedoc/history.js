'use strict'
// history
// external modules
const LZString = require('lz-string')

// core
const logger = require('./logger')
const models = require('./models')
const errors = require('./errors')

// public
const History = {
  historyGet,
  historyPost,
  historyDelete,
  updateHistory
}

function getHistory (userid, callback) {
  models.Note.findAll().then(function (notes) {
    // [{"id":"practice","text":"Practice","time":1680231818273,"tags":[]},{"id":"androi","text":"Untitled","time":1680237662879,"tags":[]},{"id":"android","text":"Android","time":1680400934755,"tags":[]}]
    // let history = {"id": "practice", "text":"test", "time":, "tags":[]}
    let history = []
    let id = 0
    let date = 0
    if (!notes) {
      return callback(null, null)
    }
    for (let i = 0, l = notes.length; i < l; i++) {
      id = notes[i].id
      history[i] = {}
      if (id && models.Note.checkNoteIdValid(id)) {
        date = notes[i].lastchangeAt !== null ? notes[i].lastchangeAt : notes[i].savedAt
        history[i].id = models.Note.encodeNoteId(id)
        history[i].text = notes[i].title
        history[i].time = Date.parse(date)
        history[i].tags = []
      }
    }
    history = parseHistoryToObject(history)
    logger.debug('read history success')
    return callback(null, history)
  }).catch(function (err) {
    logger.error('read history failed: ' + err)
    return callback(err, null)
  })
}

function setHistory (userid, history, callback) {
  models.User.update({
    history: JSON.stringify(parseHistoryToArray(history))
  }, {
    where: {
      id: userid
    }
  }).then(function (count) {
    return callback(null, count)
  }).catch(function (err) {
    logger.error('set history failed: ' + err)
    return callback(err, null)
  })
}

function updateHistory (userid, noteId, document, time) {
  if (userid && noteId && typeof document !== 'undefined') {
    getHistory(userid, function (err, history) {
      if (err || !history) return
      if (!history[noteId]) {
        history[noteId] = {}
      }
      const noteHistory = history[noteId]
      const noteInfo = models.Note.parseNoteInfo(document)
      noteHistory.id = noteId
      noteHistory.text = noteInfo.title
      noteHistory.time = time || Date.now()
      noteHistory.tags = noteInfo.tags
      setHistory(userid, history, function (err, count) {
        if (err) {
          logger.log(err)
        }
      })
    })
  }
}

function parseHistoryToArray (history) {
  const _history = []
  Object.keys(history).forEach(function (key) {
    const item = history[key]
    _history.push(item)
  })
  return _history
}

function parseHistoryToObject (history) {
  const _history = {}
  for (let i = 0, l = history.length; i < l; i++) {
    const item = history[i]
    _history[item.id] = item
  }
  return _history
}

function historyGet (req, res) {
  getHistory({}, function (err, history) {
    if (err) return errors.errorInternalError(res)
    if (!history) return errors.errorNotFound(res)
    res.send({
      history: parseHistoryToArray(history)
    })
  })
}

function historyPost (req, res) {
  if (req.isAuthenticated()) {
    const noteId = req.params.noteId
    if (!noteId) {
      if (typeof req.body.history === 'undefined') return errors.errorBadRequest(res)
      logger.debug(`SERVER received history from [${req.user.id}]: ${req.body.history}`)
      try {
        const history = JSON.parse(req.body.history)
        if (Array.isArray(history)) {
          setHistory(req.user.id, history, function (err, count) {
            if (err) return errors.errorInternalError(res)
            res.end()
          })
        } else {
          return errors.errorBadRequest(res)
        }
      } catch (err) {
        return errors.errorBadRequest(res)
      }
    } else {
      if (typeof req.body.pinned === 'undefined') return errors.errorBadRequest(res)
      getHistory(req.user.id, function (err, history) {
        if (err) return errors.errorInternalError(res)
        if (!history) return errors.errorNotFound(res)
        if (!history[noteId]) return errors.errorNotFound(res)
        if (req.body.pinned === 'true' || req.body.pinned === 'false') {
          history[noteId].pinned = (req.body.pinned === 'true')
          setHistory(req.user.id, history, function (err, count) {
            if (err) return errors.errorInternalError(res)
            res.end()
          })
        } else {
          return errors.errorBadRequest(res)
        }
      })
    }
  } else {
    return errors.errorForbidden(res)
  }
}

function historyDelete (req, res) {
  if (req.isAuthenticated()) {
    const noteId = req.params.noteId
    if (!noteId) {
      setHistory(req.user.id, [], function (err, count) {
        if (err) return errors.errorInternalError(res)
        res.end()
      })
    } else {
      getHistory(req.user.id, function (err, history) {
        if (err) return errors.errorInternalError(res)
        if (!history) return errors.errorNotFound(res)
        delete history[noteId]
        setHistory(req.user.id, history, function (err, count) {
          if (err) return errors.errorInternalError(res)
          res.end()
        })
      })
    }
  } else {
    return errors.errorForbidden(res)
  }
}

module.exports = History
